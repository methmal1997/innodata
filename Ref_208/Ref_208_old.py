print("This is Ref_208")

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

def is_first_type_p_element(p_element):
    link = p_element.find('a', href=True)
    if link and link['href'].endswith('.pdf'):
        return True
    return False

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
            Ref_value = "208"
            url_value = url.split('/')[-2]
            current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
            out_excel_file = common_function.output_excel_name(current_out)

            print("Getting latest issue. hold on .....")
            response = requests.get(url, headers=headers, timeout=100,allow_redirects=True)
            current_soup = BeautifulSoup(response.content, 'html.parser')

            special_issues = current_soup.findAll("span",class_="MsoHyperlink")
            special_issue = next((span for span in special_issues if "Special Issues" in span.get_text()), None)
            special_issue_link = "https://jestec.taylors.edu.my/"+ special_issue.find("a")["href"]

            response = requests.get(special_issue_link, headers=headers, timeout=100, allow_redirects=True)
            current_soup = BeautifulSoup(response.content, 'html.parser')
            td_elements = current_soup.find_all('td')
            pattern = re.compile(
                r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b')


            dates = []
            for td in td_elements:
                text = td.get_text(strip=True)
                match = pattern.search(text)
                if match:
                    dates.append(match.group())
            date_format = "%B %Y"
            parsed_dates = [datetime.strptime(date, date_format) for date in dates]
            latest_date = max(parsed_dates)
            latest_date = latest_date.strftime(date_format)

            p_elements = current_soup.find_all('p', class_='MsoNormal')
            for index, p in enumerate(p_elements):
                text = p.get_text(strip=True)
                if text == latest_date:
                    for span in p_elements[index:]:
                        try:
                            hyperlink_span = span.find("span", class_="MsoHyperlink").find('a')["href"]
                            part = span.find("span", class_="MsoHyperlink").find('a').text

                            pattern = r'Part\s+(\d+)'
                            match = re.search(pattern, part)
                            if match:
                                part = "Part" + match.group(1)
                            else:
                                part = ""
                        except:
                            hyperlink_span = None
                        if hyperlink_span is not None:
                            current_issue_link2 = "https://jestec.taylors.edu.my/"+hyperlink_span
                            print(current_issue_link2)
                            break
                    break

            response_special = requests.get(current_issue_link2, headers=headers, timeout=100, allow_redirects=True)
            current_soup_special = BeautifulSoup(response_special.content, 'html.parser')

            filtered_p_elements = []
            skip_index = ""
            Articles = current_soup_special.find_all('p', class_='MsoNormal')
            pdf_list = []
            for index,p in enumerate(Articles):
                span = p.find('span',
                              {'lang': 'IN', 'style': 'font-size:8.0pt; font-family:"Noto Sans Symbols";color:black'})

                if not span and index != skip_index:
                    try:
                        if p.find("a")["href"] != "about:blank":
                            if is_first_type_p_element(p):
                                Article_title = p.find("a").text.strip()
                                Article_title = ' '.join(Article_title.split())
                                Pdf_link = "https://jestec.taylors.edu.my/"+ p.find("a")["href"]
                                page_range = Articles[index + 2].get_text(strip=True)
                                print(Article_title)
                                print(Pdf_link)
                                print(page_range)
                                print(part)
                                print("##################3")

                                check_value, tpa_id = common_function.check_duplicate("", Article_title, url_id, "",
                                                                                      "")

                                if Check_duplicate.lower() == "true" and check_value:
                                    message = f"{Pdf_link} - duplicate record with TPAID : {tpa_id}"
                                    duplicate_list.append(message)
                                    print("Duplicate Article :", Pdf_link)
                                else:
                                    if Article_title not in pdf_list:
                                        response_2 = requests.get(Pdf_link, headers=headers, timeout=100,verify=False)
                                        pdf_content = response_2.content
                                        output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                                        with open(output_fimeName, 'wb') as file:
                                            file.write(pdf_content)

                                        data.append(
                                            {"Title": Article_title, "DOI": "",
                                             "Publisher Item Type": "",
                                             "ItemID": "",
                                             "Identifier": "",
                                             "Volume": "", "Issue": "", "Supplement": "",
                                             "Part": part,
                                             "Special Issue": "Special_Issue", "Page Range": page_range, "Month": "",
                                             "Day": "",
                                             "Year": "",
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
                    except:
                        pass

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