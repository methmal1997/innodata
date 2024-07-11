print("This is Ref_136")

import re
import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import certifi
import os
import sys
from datetime import datetime
import common_function
import pandas as pd
from PyPDF2 import PdfReader
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

duplicate_list = []
error_list = []
completed_list = []
attachment=None
url_id=None
current_date=None
current_time=None
Ref_value=None
ini_path=None


try:
    print("Process started...")
    print("This may take sometime.Please wait..........")

    try:
        with open('urlDetails.txt', 'r', encoding='utf-8') as file:
            url_list = file.read().split('\n')
    except Exception as error:
        Error_message = "Error in the \"urlDetails\" : " + str(error)
        print(Error_message)
        error_list.append(Error_message)
        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                             len(completed_list),
                                             ini_path, attachment, current_date, current_time, Ref_value)

    for i, url_url_id in enumerate(url_list):

        try:
            url, url_id = url_url_id.split(',')
            print(f"Executing this {url}")
            current_datetime = datetime.now()
            current_date = str(current_datetime.date())
            current_time = current_datetime.strftime("%H:%M:%S")

            ini_path = os.path.join(os.getcwd(), "Info.ini")
            Download_Path, Email_Sent, Check_duplicate, user_id = common_function.read_ini_file(ini_path)

            data = []
            pdf_count = 1
            Ref_value = "136"
            url_value = url.split('/')[-2]
            current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
            out_excel_file = common_function.output_excel_name(current_out)
            response = requests.get(url, headers=headers, timeout=50,verify=False)
            current_soup = BeautifulSoup(response.content, 'html.parser')
            target_div = current_soup.find('div', class_="yw_text_small persian").findAll('a', href=True)[-1]
            latest_issue_url = "https://fsct.modares.ac.ir/"+target_div['href']

            response_2 = requests.get(latest_issue_url, headers=headers, timeout=50, verify=False)
            current_soup_2 = BeautifulSoup(response_2.content, 'html.parser')
            vol_issue = current_soup_2.find('div', class_="yw_text persian").text.strip()
            match = re.search(r"Volume (\d+), Issue (\d+) \((\d{4})\)", vol_issue)
            volume = match.group(1)
            issue = match.group(2)
            year = match.group(3)

            articles = current_soup_2.find_all('div', class_='yw_text')
            filtered_articles = [article for article in articles if
                                 article.find('span', style='vertical-align:middle; direction:ltr')]

            filtered_articles = list(set(filtered_articles))
            pdf_list = []

            articles_count_with_pdf = len(filtered_articles)
            print(f"articles_count_with_pdf {articles_count_with_pdf}")
            for article in filtered_articles:
                try:
                    Article_title = article.find('div', class_="yw_text yw_col1").text.strip()
                    page_range = article.find('div', class_="yw_text yw_col2 persian").text.strip()
                    page_range = re.search(r"P\.\s*(\d+-\d+)", page_range).group(1)
                    sp = str(article.find('span', style='vertical-align:middle; direction:ltr').text.strip())
                    DOI = sp[8:]

                    pdf = article.find('div',class_='yw_text_med persian').findAll('a')[2]['href'][1:]
                    Pdf_link = "https://fsct.modares.ac.ir" + pdf
                    print(Article_title)
                    check_value, tpa_id = common_function.check_duplicate(DOI, Pdf_link, url_id, volume, issue)

                    if Check_duplicate.lower() == "true" and check_value:
                        message = f"{Pdf_link} - duplicate record with TPAID : {tpa_id}"
                        duplicate_list.append(message)
                        print("Duplicate Article :", Pdf_link)
                    else:
                        response_2 = requests.get(Pdf_link, headers=headers, timeout=50,verify=False)
                        pdf_content = response_2.content
                        output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                        with open(output_fimeName, 'wb') as file:
                            file.write(pdf_content)

                        data.append(
                            {"Title": Article_title, "DOI": DOI,
                             "Publisher Item Type": "",
                             "ItemID": "",
                             "Identifier": "",
                             "Volume": volume, "Issue": issue, "Supplement": "",
                             "Part": "",
                             "Special Issue": "", "Page Range": page_range, "Month": '',
                             "Day": "",
                             "Year": year,
                             "URL": Pdf_link,
                             "SOURCE File Name": f"{pdf_count}.pdf",
                             "user_id": user_id})

                        df = pd.DataFrame(data)
                        df.to_excel(out_excel_file, index=False)
                        print(f"Downloaded the PDF file {pdf_count}")
                        pdf_count += 1
                        completed_list.append(Pdf_link)
                        with open('completed.txt', 'a', encoding='utf-8') as write_file:
                            write_file.write(Pdf_link + '\n')
                        pdf_list.append(Article_title)

                except Exception as error:
                    Error_message = "Error in the article downloading:" + str(error)
                    print(Error_message, "\n")
                    error_list.append(Error_message)
                    common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                         len(completed_list),
                                                         ini_path, attachment, current_date, current_time,
                                                         Ref_value)

            try:
                common_function.sendCountAsPost(url_id, Ref_value, str(articles_count_with_pdf),
                                                str(len(completed_list)),
                                                str(len(duplicate_list)),
                                                str(len(error_list)))
            except Exception as error:
                message = str(error)
                print("New update")
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

        except Exception as error:
            Error_message = f"Error in the site: {error}"
            print(Error_message, "\n")
            error_list.append(Error_message)
            common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                 len(completed_list),
                                                 ini_path, attachment, current_date, current_time, Ref_value)

except:
    Error_message = "Error in the main process :"

    error_list.append(str(Error_message))
    log_file_path = os.path.join('log.txt')
    with open(log_file_path, 'w') as log_file:
        log_file.write(str(Error_message) + '\n')