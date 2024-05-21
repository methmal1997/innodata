import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from urllib.parse import urljoin
from datetime import datetime
import os
import common_function
from googletrans import Translator

url_id = "939594939"

translator = Translator()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

duplicate_list = []
error_list = []
completed_list = []
attachment = None
current_date = None
current_time = None
Ref_value = None
time_prefix = None
today_date = None
ini_path = None

try:
    with open('completed.txt', 'r', encoding='utf-8') as read_file:
        read_content = read_file.read().split('\n')
except FileNotFoundError:
    with open('completed.txt', 'w', encoding='utf-8'):
        with open('completed.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().split('\n')

try:
    base_url = "http://www.suidaojs.com/EN/"
    url = "http://www.suidaojs.com/EN/2096-4498/home.shtml"

    current_datetime = datetime.now()
    current_date = str(current_datetime.date())
    current_time = current_datetime.strftime("%H:%M:%S")

    ini_path = os.path.join(os.getcwd(), "Info.ini")
    Download_Path, Email_Sent, Check_duplicate, user_id = common_function.read_ini_file(ini_path)
    current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
    out_excel_file = common_function.output_excel_name(current_out)
    Ref_value = "46"
    print(url_id)

    duplicate_list = []
    error_list = []
    completed_list = []
    data = []
    pdf_count = 1

    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    div_element = soup.find("div", class_="article-list").findAll("ul")

    for single_element in div_element:
        article_link, article_title = None, None
        try:
            article_title = single_element.find("div", class_="j-title").text.strip()
            translated_title = translator.translate(article_title, src='auto', dest='en').text

            article_link = single_element.find("div", class_="j-title").find('a').get('href')
            if not article_link in read_content:

                onclick_attr = single_element.find("span", class_="j-pdf").find("a").get("onclick")
                ids = re.search(r"lsdy1\('PDF','(\d+)','http://www.suidaojs.com'", onclick_attr).group(1)

                base_pdf_url = "http://www.suidaojs.com/EN/article/downloadArticleFile.do?attachType=PDF&id="

                pdf_url = base_pdf_url + str(ids)

                doi = single_element.find("div", class_="j-date").text.strip().split(":")[-1].strip()

                volume_issue_text = single_element.find("div", class_="j-date").text.strip()
                match = re.match(r'(\d{4}), (\d+)\((\d+)\): (.+)', volume_issue_text)
                year, volume, issue = "", "", ""
                if match:
                    year = match.group(1)
                    volume = match.group(2)
                    issue = match.group(3)

                page_range = single_element.find("div", class_="j-date").find("span").text.strip().split(":")[-1].strip()

                check_value = common_function.check_duplicate(doi, article_title, url_id, volume, issue)
                if Check_duplicate.lower() == "true" and check_value:
                    message = f"{article_title} - duplicate record with TPAID {{tpaid returned in response}}"
                    duplicate_list.append(message)
                    print("Duplicate Article :", translated_title)

                else:
                    pdf_content = requests.get(pdf_url, headers=headers, verify=False).content
                    output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                    with open(output_fimeName, 'wb') as file:
                        file.write(pdf_content)
                    data.append(
                        {"Title": translated_title, "DOI": doi, "Publisher Item Type": "", "ItemID": "",
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
        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                             len(completed_list), ini_path, attachment, current_date,
                                             current_time, Ref_value)

    sts_file_path = os.path.join(current_out, 'Completed.sts')
    with open(sts_file_path, 'w') as sts_file:
        pass


except Exception as e:
    Error_message = "Error in the site :" + str(e)
    print(Error_message)
    error_list.append(Error_message)
    common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list, len(completed_list),
                                         ini_path, attachment, current_date, current_time, Ref_value)
