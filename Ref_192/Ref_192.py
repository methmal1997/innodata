print("This is Ref_192")

import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# import undetected_chromedriver as uc
# import chromedriver_autoinstaller as chromedriver
# chromedriver.install()
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
            Ref_value = "192"
            url_value = url.split('/')[-2]
            current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
            out_excel_file = common_function.output_excel_name(current_out)

            url2 = url + "/content/current"
            print(url)
            response = requests.get(url2, headers=headers, timeout=50,allow_redirects=True)
            current_soup = BeautifulSoup(response.content, 'html.parser')

            month_year = current_soup.find('span', class_='highwire-cite-metadata-pub-date').text.strip().split()
            month = month_year[0]
            year = month_year[1].rstrip(';')

            volume = current_soup.find('span', class_='highwire-cite-metadata-volume').text.strip().replace('Volume ',                                                                                       '').rstrip(',')
            issue = current_soup.find('span', class_='highwire-cite-metadata-issue').text.strip().replace('Issue ', '')

            print("month =", month)
            print("year =", year)
            print("Volume =", volume)
            print("Issue =", issue)
            p = "highwire-foxycart-add-to-cart-ahah highwire-foxycart-add-to-cart-ahah"
            sections = list(set(current_soup.findAll('a', class_='highwire-cite-linked-title')))
            linked_title_divs = current_soup.find_all('a', class_='highwire-cite-linked-title')

            pdf_list = []

            for div in linked_title_divs:
                parent_div = div.find_parent('div', class_='toc-citation')
                if parent_div and parent_div.find('span', class_='highwire-foxycart-add-to-cart-ahah'):
                    Article_title = parent_div.find("span",class_="highwire-cite-title").text
                    page_range = parent_div.find("span",class_="highwire-cite-metadata-pages highwire-cite-metadata").text

                    doi_element = parent_div.find("span", class_="highwire-cite-metadata-doi highwire-cite-metadata").text
                    DOI = '/'.join(doi_element.split('/')[-2:])
                    DOI += ' '

                    Article_link = url + parent_div.find("a", class_="highwire-cite-linked-title")['href']

                    response = requests.get(Article_link, headers=headers, timeout=50, allow_redirects=True)
                    current_soup = BeautifulSoup(response.content, 'html.parser')

                    Pdf_link = current_soup.find('a', class_="highwire-article-nav-jumplink")["href"].replace("/content", "")
                    Pdf_link = "https://ar.iiarjournals.org/content/anticanres" + Pdf_link + ".full.pdf"

                    check_value, tpa_id = common_function.check_duplicate(DOI, Pdf_link, url_id, volume, issue)

                    if Check_duplicate.lower() == "true" and check_value:
                        message = f"{Pdf_link} - duplicate record with TPAID : {tpa_id}"
                        duplicate_list.append(message)
                        print("Duplicate Article :", Pdf_link)
                    else:
                        if Article_title not in pdf_list:
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
                                 "Special Issue": "", "Page Range": page_range, "Month": month,
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
                            print("###################################")

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