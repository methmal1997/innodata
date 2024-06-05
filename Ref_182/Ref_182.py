print("This is Ref_136")

import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re
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


def get_current_issue():

    response=requests.post("http://www.cjco.cn/data/catalog/catalogMap")
    soup=json.loads(BeautifulSoup(response.content,'html.parser').text)
    year_key = str(list(soup["data"]["archive_list"].keys())[0])
    issue=soup["data"]["archive_list"][year_key][0]["issue"]
    link=f"http://www.cjco.cn/cn/article/{year_key}/{issue}"

    return link


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
            Ref_value = "182"
            url_value = url.split('/')[-2]
            current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
            out_excel_file = common_function.output_excel_name(current_out)
            issue_url = url + "issues"
            response = requests.get(issue_url, headers=headers, timeout=50)
            current_soup = BeautifulSoup(response.content, 'html.parser')
            currnt_part = current_soup.find("ul",class_="issues-li").find('li',class_="issues-li-item").find('a')["href"]
            current_url = url + currnt_part
            response = requests.get(current_url, headers=headers, timeout=50)
            current_soup = BeautifulSoup(response.content, 'html.parser')
            vol_year = current_soup.find('h2', class_='h3 mt-0').text.strip().split()

            year = vol_year[2][1:-1]
            volume = vol_year[1]
            print(volume)
            print(year)

            articles = current_soup.findAll('a',class_="title-link")
            print(len(articles))
            for article in articles:
                print(article.text)

            # Extract the links
            # for link in links_2024.find_all('a', href=True):
            #     print(link['href'])

            # article_list =current_soup.findAll('div',class_="article-list")
            # pdf_list = []
            # for article in article_list:
            #     print("################################################################")
            #
            #     pub_info_element = article.find('div', class_='article-list-time').find('font')
            #     pub_info = pub_info_element.get_text(strip=True)
            #     pattern = r"(\d{4}), (\d+)\((\d+)\): (\d+-\d+)"
            #     match = re.search(pattern, pub_info)
            #     year, volume, issue, page_range = match.groups()
            #
            #     title_element = article.find('div', class_='article-list-title').find('a', href=True)
            #     url_part = title_element['href']
            #     Article_link = "http://www.cjco.cn/" + url_part
            #
            #     Article_title = title_element.get_text(strip=True)
            #     # doi_element = article.find('a', href=True, string=True)
            #     # DOI = doi_element['href'].split('/doi/')[-1]
            #     response = requests.get(Article_link, headers=headers, timeout=50)
            #     current_soup = BeautifulSoup(response.content, 'html.parser')
            #     dc_identifier_meta = current_soup.find('meta', attrs={'name': 'dc.identifier'})
            #     DOI = dc_identifier_meta['content']
            #
            #     pdf_element = article.find('div', class_='article-list-zy').find('font', class_='font3').find('a',                                                                                            onclick=True)
            #     if pdf_element:
            #         pdf_onclick = pdf_element['onclick']
            #     pdf_id_match = re.search(r"downloadpdf\('(.+?)'\)", pdf_onclick)
            #     if pdf_id_match:
            #         pdf_id = pdf_id_match.group(1)
            #
            #     Pdf_link = f"http://www.cjco.cn/article/exportPdf?id={pdf_id}"
            #     check_value, tpa_id = common_function.check_duplicate(DOI, Pdf_link, url_id, volume, issue)
            #
            #     if Check_duplicate.lower() == "true" and check_value:
            #         message = f"{Pdf_link} - duplicate record with TPAID : {tpa_id}"
            #         duplicate_list.append(message)
            #         print("Duplicate Article :", Pdf_link)
            #     else:
            #         if Article_title not in pdf_list:
            #             response_2 = requests.get(Pdf_link, headers=headers, timeout=50,verify=False)
            #             pdf_content = response_2.content
            #             output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
            #             with open(output_fimeName, 'wb') as file:
            #                 file.write(pdf_content)
            #
            #             data.append(
            #                 {"Title": Article_title, "DOI": DOI,
            #                  "Publisher Item Type": "",
            #                  "ItemID": "",
            #                  "Identifier": "",
            #                  "Volume": volume, "Issue": issue, "Supplement": "",
            #                  "Part": "",
            #                  "Special Issue": "", "Page Range": "", "Month": '',
            #                  "Day": "",
            #                  "Year": year,
            #                  "URL": Pdf_link,
            #                  "SOURCE File Name": f"{pdf_count}.pdf",
            #                  "user_id": user_id})
            #
            #             df = pd.DataFrame(data)
            #             df.to_excel(out_excel_file, index=False)
            #             print(f"Downloaded the PDF file {pdf_count}")
            #             pdf_count += 1
            #             completed_list.append(Pdf_link)
            #             with open('completed.txt', 'a', encoding='utf-8') as write_file:
            #                 write_file.write(Pdf_link + '\n')
            #             pdf_list.append(Article_title)

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