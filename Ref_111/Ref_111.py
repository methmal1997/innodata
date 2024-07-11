import warnings
warnings.filterwarnings('ignore')

print("This is Ref_111")

import re
import random
import time
import requests
from bs4 import BeautifulSoup
import os
import common_function
from datetime import datetime
import pandas as pd
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

duplicate_list = []
error_list = []
completed_list = []
attachment = None
url_id = None
current_date = None
current_time = None
Ref_value = None
ini_path = None

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

proxies_list = [
    "141.98.155.137:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.205.199.161:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "216.10.5.126:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "2.58.80.143:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.207.96.233:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "67.227.121.110:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "67.227.127.100:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "181.177.76.122:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.207.97.85:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "186.179.21.77:3199:mariyarathna-dh3w3:IxjkW0fdJy"
]

formatted_proxies = []
for proxy in proxies_list:
    ip, port, user, password = proxy.split(':')
    formatted_proxy = f'http://{user}:{password}@{ip}:{port}'
    formatted_proxies.append({'http': formatted_proxy, 'https': formatted_proxy})

try:

    with open('urlDetails.txt', 'r', encoding='utf-8') as file:
        url_list = file.read().split('\n')
    print("Process started...")
    print("This may take sometime.Please wait..........")
    print("Urldetails text file was readed......")
    try:
        with open('completed.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().split('\n')
    except FileNotFoundError:
        with open('completed.txt', 'w', encoding='utf-8'):
            with open('completed.txt', 'r', encoding='utf-8') as read_file:
                read_content = read_file.read().split('\n')


    for i, url_url_id in enumerate(url_list):
        try:
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
                Ref_value = "111"
                url_value = url.split('/')[-2]

                current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
                out_excel_file = common_function.output_excel_name(current_out)

                response = requests.get(url, headers=headers, timeout=20)
                current_soup = BeautifulSoup(response.content, 'html.parser')
                l2_container = current_soup.find_all('div', class_='L2-container')[2]
                l3_item_url = 'https://medic.upm.edu.my'+l2_container.find_all('li', class_='L3-item')[0].find('a').get('href')

                # l3_item_url = "https://medic.upm.edu.my/jurnal_kami/volume_20_2024/mjmhs_vol20_supp_3_may_2024-79575"
                response_2 = requests.get(l3_item_url, headers=headers, timeout=20)
                current_soup_2 = BeautifulSoup(response_2.content, 'html.parser')
                vol_issue = current_soup_2.find('h1', class_='L3-title').text
                pattern = r"VOL\.(\d+)\sSUPP\s(\d+)\s-\s([A-Z]+)\s(\d{4})"
                pattern2 = r"VOL\.(\d+)\sNO\.(\d+)\s-\s([A-Z]+)\s(\d{4})"
                match = re.search(pattern, vol_issue)
                match2 = re.search(pattern2, vol_issue)
                issue = ''
                supplement = ''
                pdf_list = []
                if match:

                    volume = match.group(1)
                    supplement = match.group(2)
                    month = match.group(3)
                    year = match.group(4)
                elif match2:
                    volume = match2.group(1)
                    issue = match2.group(2)
                    month = match2.group(3)
                    year = match2.group(4)
                print(volume)
                print(issue)
                print(month)
                print(year)
                print(supplement)


                p_tags = current_soup_2.find_all('p')
                pattern = re.compile(r'^\d+\.\s')

                filtered_p_tags = [p for p in p_tags if p.find(text=pattern)]

                No_of_Articles = []

                for p in filtered_p_tags:
                    try:
                        Article = p.find('a').get('href')
                        No_of_Articles.append(Article)

                        Article_title = p.text.split('http')[0].strip().split('.', 1)[1].strip().replace('"', '').split(':')[0].strip()
                        DOI = p.text.split("://")[1].split("doi.org/")[1].split('\n')[0]
                        Pdf_link = 'https://medic.upm.edu.my/'+ p.find('a').get('href')
                        # print(DOI)

                        check_value, tpa_id = common_function.check_duplicate(DOI, Pdf_link, url_id, volume, issue)

                        if issue == '':
                            check_value, tpa_id = common_function.check_duplicate(DOI, Pdf_link, url_id, volume, supplement)

                        if Check_duplicate.lower() == "true" and check_value:
                            message = f"{Pdf_link} - duplicate record with TPAID : {tpa_id}"
                            duplicate_list.append(message)
                            print("Duplicate Article :", Pdf_link)

                        else:
                            if Article_title not in pdf_list:
                                response = requests.get(Pdf_link, headers=headers, timeout=20)
                                pdf_content = response.content
                                output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                                with open(output_fimeName, 'wb') as file:
                                    file.write(pdf_content)

                                data.append(
                                    {"Title": Article_title, "DOI": DOI,
                                     "Publisher Item Type": "",
                                     "ItemID": "",
                                     "Identifier": "",
                                     "Volume": volume, "Issue": issue, "Supplement": supplement,
                                     "Part": "",
                                     "Special Issue": "", "Page Range": "", "Month": month,
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

                    articles_count_with_pdf = len(No_of_Articles)
                    if articles_count_with_pdf==0:
                        print("no pdf in site")

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
                Error_message = "Error in the site:" + str(error)
                print(Error_message, "\n")
                error_list.append(Error_message)
                common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                     len(completed_list),
                                                     ini_path, attachment, current_date, current_time, Ref_value)
        except:
            pass


except:
    Error_message = "Error in the main process :"

    error_list.append(str(Error_message))
    log_file_path = os.path.join('log.txt')
    with open(log_file_path, 'w') as log_file:
        log_file.write(str(Error_message) + '\n')
