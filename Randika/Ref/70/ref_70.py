import os
import requests
from bs4 import BeautifulSoup
import common_function
import pandas as pd
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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
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


    try:
        with open('completed.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().split('\n')
    except FileNotFoundError:
        with open('completed.txt', 'w', encoding='utf-8'):
            with open('completed.txt', 'r', encoding='utf-8') as read_file:
                read_content = read_file.read().split('\n')

    for line in url_details:
        try:
            url, source_id = line.strip().split(",")

            current_datetime = datetime.now()
            current_date = str(current_datetime.date())
            current_time = current_datetime.strftime("%H:%M:%S")

            ini_path = os.path.join(os.getcwd(), "Info.ini")
            Download_Path, Email_Sent, Check_duplicate, user_id = common_function.read_ini_file(ini_path)
            current_out = common_function.return_current_outfolder(Download_Path, user_id, source_id)
            out_excel_file = common_function.output_excel_name(current_out)
            Ref_value = "70"
            print(source_id)

            duplicate_list = []
            error_list = []
            completed_list = []
            data = []
            pdf_count = 1

            response = requests.get(url, headers=headers)
            if url == "https://revistas.unav.edu/index.php/estudios-sobre-educacion/issue/archive" or "https://revistas.unav.edu/index.php/anuario-filosofico/issue/archive":
                current_link = BeautifulSoup(response.content, "html.parser").find("div", class_="issues media-list").findAll("h2", class_="media-heading")[1].find("a", class_="title").get("href")

            else:
                current_link = BeautifulSoup(response.content, "html.parser").find("div", class_="issues media-list").find("h2", class_="media-heading").find("a", class_="title").get("href")

            response = requests.get(current_link, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                div_section = soup.find("div", class_="sections").findAll("div", class_="article-summary media")

                for single_section in div_section:
                    article_link, article_title = None, None
                    try:
                        article_title = single_section.find("h3", class_="media-heading").text.strip()

                        article_link = single_section.find("h3", class_="media-heading").find("a").get("href")
                        page_range = single_section.find("span", class_="pull-right unav-pages").text.strip()

                        active_li = soup.find("li", class_="active")
                        active_text = active_li.text.strip()
                        parts = active_text.split()

                        if len(parts) >= 4:
                            volume = parts[1]
                            issue = parts[3]
                            year = parts[4].rstrip(')').replace('(', '').replace(')', '').replace(':',
                                                                                                  '')
                            article_response = requests.get(article_link)
                            if article_response.status_code == 200:
                                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                                doi_tag = article_soup.find('div', class_='list-group-item doi')
                                doi = ""
                                if doi_tag:
                                    doi_link = doi_tag.find('a')
                                    if doi_link:
                                        doi = doi_link['href']
                                        doi = doi.replace("https://doi.org/", "")

                                last_page_link = single_section.find("div", class_="btn-group btn-group-unav-summary pull-right").find("a", class_="galley-link btn btn-primary pdf").get('href')

                                last_response = requests.get(last_page_link, headers=headers)
                                if last_response.status_code == 200:
                                    last_soup = BeautifulSoup(last_response.text, "html.parser")
                                    pdf_url_tag = last_soup.find("a", class_="download")
                                    if pdf_url_tag:
                                        pdf_url = pdf_url_tag.get("href")
                                        pdf_content = requests.get(pdf_url, headers=headers).content
                                        output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                                        with open(output_fimeName, 'wb') as file:
                                            file.write(pdf_content)
                                        data.append(
                                            {"Title": article_title, "DOI": doi, "Publisher Item Type": "", "ItemID": "",
                                             "Identifier": "",
                                             "Volume": volume, "Issue": issue, "Supplement": "", "Part": "",
                                             "Special Issue": "", "Page Range": page_range, "Month": "", "Day": "",
                                             "Year": year,
                                             "URL": article_link, "SOURCE File Name": f"{pdf_count}.pdf", "user_id": user_id})
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
