import os
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import common_function
from datetime import datetime

duplicate_list = []
error_list = []
completed_list = []
attachment = None
current_date = None
current_time = None
Ref_value = None
source_id = None
time_prefix = None
today_date = None
ini_path = None

month_mapping = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

try:
    try:
        with open('urlDetails.txt', 'r', encoding='utf-8') as file:
            url_details = file.readlines()
    except Exception as error:
        Error_message = "Error in the urlDetails.txt file :" + str(error)
        print(Error_message)
        error_list.append(Error_message)
        common_function.attachment_for_email(source_id, duplicate_list, error_list, completed_list, len(completed_list),
                                             ini_path, attachment, current_date, current_time, Ref_value)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    try:
        with open('completed.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().split('\n')
    except FileNotFoundError:
        with open('completed.txt', 'w', encoding='utf-8'):
            with open('completed.txt', 'r', encoding='utf-8') as read_file:
                read_content = read_file.read().split('\n')

    for line in url_details:
        try:
            if ',' in line:
                url, source_id = line.strip().split(",", 1)
                source_id = source_id.strip()
            else:
                continue

            response = requests.get(url, headers=headers)
            # print("URL:", url)
            # print("Response status code:", response.status_code)

            current_datetime = datetime.now()
            current_date = str(current_datetime.date())
            current_time = current_datetime.strftime("%H:%M:%S")

            ini_path = os.path.join(os.getcwd(), "Info.ini")
            Download_Path, Email_Sent, Check_duplicate, user_id = common_function.read_ini_file(ini_path)
            current_out = common_function.return_current_outfolder(Download_Path, user_id, source_id)
            out_excel_file = common_function.output_excel_name(current_out)
            Ref_value = "67"
            print(source_id)

            duplicate_list = []
            error_list = []
            completed_list = []
            data = []
            pdf_count = 1

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                for title_element in soup.find_all('h1', class_='typography-body text-display4 font-ui fw-3 color-primary f-4 ln-3'):
                    article_link, article_title = None, None
                    try:
                        article_title = title_element.text.strip()
                        url_element = title_element.find('a')
                        if url_element:
                            article_link = "https://journals.ametsoc.org" + url_element.get('href')
                            if not article_link in read_content:

                                pdf_urls = article_link.replace("/view/", "/downloadpdf/")
                                pdf_link = pdf_urls.replace(".xml", ".pdf")

                                pdf_url = pdf_link.replace("/downloadpdf/", "/downloadpdf/view/")

                                doi_elements = title_element.find_all('a', class_='c-Button--link', href=True)
                                dois = [f"10.1175/{doi_element['href'].split('/')[-1].replace('.xml', '')}" for doi_element in
                                        doi_elements]
                                dois = ', '.join(dois)

                                issu_info = soup.find('h1', class_='typography-body title mb-3 text-headline font-content')

                                volume, issue, year, month_full = "", "", "", ""
                                if issu_info:
                                    issu_text = issu_info.text.strip()
                                    match = re.search(r'Volume (\d+) \((\d{4})\): Issue (\d+) \((\w{3}) (\d{4})\)', issu_text)

                                    if match:
                                        volume = match.group(1)
                                        year = match.group(2)
                                        issue = match.group(3)
                                        month_abbreviated = match.group(4)
                                        month_full = month_mapping.get(month_abbreviated, month_abbreviated)

                                page_range_element = title_element.find_next("dd",
                                                                             class_="pagerange inline c-List__item c-List__item--secondary text-metadata-value")

                                page_range = ""
                                if page_range_element:
                                    page_range = page_range_element.text.strip()

                                check_value = common_function.check_duplicate(dois, article_title, source_id, volume, issue)
                                if Check_duplicate.lower() == "true" and check_value:
                                    message = f"{article_title} - duplicate record with TPAID {{tpaid returned in response}}"
                                    duplicate_list.append(message)
                                    print("Duplicate Article :", article_title)

                                else:
                                    pdf_content = requests.get(pdf_url, headers=headers).content
                                    output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                                    with open(output_fimeName, 'wb') as file:
                                        file.write(pdf_content)
                                    data.append(
                                        {"Title": article_title, "DOI": dois, "Publisher Item Type": "", "ItemID": "",
                                         "Identifier": "",
                                         "Volume": volume, "Issue": issue, "Supplement": "", "Part": "",
                                         "Special Issue": "", "Page Range": page_range, "Month": "", "Day": "",
                                         "Year": year,
                                         "URL": article_link, "SOURCE File Name": f"{pdf_count}.pdf",
                                         "user_id": user_id})
                                    df = pd.DataFrame(data)
                                    df.to_excel(out_excel_file, index=False)
                                    pdf_count += 1
                                    scrape_message = f"{article_link}"
                                    completed_list.append(scrape_message)
                                    with open('completed.txt', 'a', encoding='utf-8') as write_file:
                                        write_file.write(article_link + '\n')
                                    print("Original Article :", article_link)

                    except Exception as error:
                        message = f"Error link - {article_title} : {str(error)}"
                        print(f"{article_title} : {str(error)}")
                        error_list.append(message)

                if str(Email_Sent).lower() == "true":
                    attachment_path = out_excel_file
                    if os.path.isfile(attachment_path):
                        attachment = attachment_path
                    else:
                        attachment = None
                    common_function.attachment_for_email(source_id, duplicate_list, error_list, completed_list,
                                                         len(completed_list), ini_path, attachment, current_date,
                                                         current_time, Ref_value)
                sts_file_path = os.path.join(current_out, 'Completed.sts')
                with open(sts_file_path, 'w') as sts_file:
                    pass

        except Exception as e:
            Error_message = "Error in the site :" + str(e)
            print(Error_message)
            error_list.append(Error_message)
            common_function.attachment_for_email(source_id, duplicate_list, error_list, completed_list, len(completed_list),
                                                 ini_path, attachment, current_date, current_time, Ref_value)

except Exception as error:
    Error_message = "Error in the urlDetails.txt file :" + str(error)
    print(Error_message)
    error_list.append(Error_message)
    common_function.attachment_for_email(source_id, duplicate_list, error_list, completed_list, len(completed_list),
                                         ini_path, attachment, current_date, current_time, Ref_value)
