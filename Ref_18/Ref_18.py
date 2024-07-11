print("This is Ref_18")


import random
import re
import time

import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import common_function
import pandas as pd
import captcha_main
import chromedriver_autoinstaller as chromedriver
chromedriver.install()
from urllib.parse import urlparse

import warnings
warnings.filterwarnings("ignore")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
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

def get_soup(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
def get_random_proxy():
    return random.choice(formatted_proxies)

def get_request_article(Article_link):
    try:
        response = requests.get(Article_link, headers=headers)
        current_soup_2 = BeautifulSoup(response.content, 'html.parser')
        path_parts = urlparse(current_soup_2.find('a', property="sameAs").text).path.split('/')
        DOI = '/'.join(path_parts[1:])
        Indentifier = current_soup_2.find('span', property="identifier").text
    except:
        try:
            response = requests.get(Article_link, proxies=get_random_proxy(), headers=headers)
            current_soup_2 = BeautifulSoup(response.content, 'html.parser')
            path_parts = urlparse(current_soup_2.find('a', property="sameAs").text).path.split('/')
            DOI = '/'.join(path_parts[1:])
            Indentifier = current_soup_2.find('span', property="identifier").text
        except:
            try:
                response = captcha_main.captcha_main(Article_link)
                current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                path_parts = urlparse(current_soup_2.find('a', property="sameAs").text).path.split('/')
                DOI = '/'.join(path_parts[1:])
                Indentifier = current_soup_2.find('span', property="identifier").text

            except Exception as error:
                Error_message = "Error in captcha. please check captcha_api.txt with correct key and token :" + str(
                    error)
                print(response.content)
                print(f"couldn't able load article {Article_link}")
    return response


duplicate_list = []
error_list = []
completed_list = []
attachment = None
url_id = None
current_date = None
current_time = None
Ref_value = None
ini_path = None

try:
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

                url, url_id = url_url_id.split(',')
                print(f"Executing this {url}")
                current_datetime = datetime.now()
                current_date = str(current_datetime.date())
                current_time = current_datetime.strftime("%H:%M:%S")

                ini_path = os.path.join(os.getcwd(), "Info.ini")
                Download_Path, Email_Sent, Check_duplicate, user_id = common_function.read_ini_file(ini_path)
                duplicate_list = []
                error_list = []
                completed_list = []
                data = []
                pdf_count = 1
                Ref_value = "18"
                url_value = url.split('/')[-2]

                current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
                out_excel_file = common_function.output_excel_name(current_out)

                try:
                    try:
                        current_soup = get_soup(url)
                        date_element = current_soup.find('span', class_='pr-2 mr-2 border-right border-deep-gray')
                        month, day, year = date_element.text.split()
                    except:
                        try:
                            print("Normal request failed, trying proxy...")
                            response = requests.get(url, proxies=get_random_proxy(), headers=headers)
                            current_soup = BeautifulSoup(response.content, 'html.parser')
                            month, day, year = date_element.text.split()
                        except:
                            try:
                                print("Proxy failed. trying captcha slover...")
                                response = captcha_main.captcha_main(url)
                                current_soup = BeautifulSoup(response.content, 'html.parser')
                                month, day, year = date_element.text.split()
                            except Exception as error:
                                Error_message = f"Error in captcha.failed to load {url}"
                                print(Error_message)
                                print("Retring.......")
                                trial_0 = 1
                                approach_0 = True
                                while approach_0:
                                    time.sleep(random.randint(5, 10))
                                    response = get_request_article(url)
                                    print("Retring.......")
                                    trial_0 = trial_0 + 1
                                    if response.status_code == 200:
                                        approach_0 = False
                                        break
                                    elif trial_0 == 4:
                                        Error_message = f"Error in captcha. please check captcha_api.txt with correct key and token"
                                        print(f"unbale to load {url}")
                                        error_list.append(Error_message)
                                        approach = False
                                        break

                    day = day[:-1]
                    vol_element = date_element.find_next('span', class_='pr-2 mr-2 border-right border-deep-gray')
                    volume = vol_element.text.strip().split()[-1]
                    issue = vol_element.find_next('span').text.strip().split()[-1]

                    All_articles = current_soup.findAll('a', class_='text-reset animation-underline')
                    no_of_articles = len(All_articles)
                    print(f"The total number of PDFs are {no_of_articles}")
                    status = 1
                    for article in All_articles:
                        Article_link, Article_title = None, None
                        Article_title = str(article.text).strip()
                        Article_link = "https://www.pnas.org" + article.get('href')

                        try:
                            response = requests.get(Article_link, headers=headers)
                            current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                            path_parts = urlparse(current_soup_2.find('a', property="sameAs").text).path.split('/')
                            DOI = '/'.join(path_parts[1:])
                            Indentifier = current_soup_2.find('span', property="identifier").text
                        except:
                            try:
                                response = requests.get(Article_link, proxies=get_random_proxy(), headers=headers)
                                current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                                path_parts = urlparse(current_soup_2.find('a', property="sameAs").text).path.split('/')
                                DOI = '/'.join(path_parts[1:])
                                Indentifier = current_soup_2.find('span', property="identifier").text
                            except:
                                try:
                                    response = captcha_main.captcha_main(Article_link)
                                    current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                                    path_parts = urlparse(current_soup_2.find('a', property="sameAs").text).path.split('/')
                                    DOI = '/'.join(path_parts[1:])
                                    Indentifier = current_soup_2.find('span', property="identifier").text


                                except Exception as error:
                                    Error_message = f"Error in captcha.failed to load {Article_link}"
                                    print("Retring.......")
                                    approach = True
                                    trial = 1
                                    while approach:
                                        time.sleep(random.randint(5, 10))
                                        response = get_request_article(Article_link)
                                        print("Retring.......")
                                        trial = trial+1
                                        if response.status_code == 200:
                                            approach = False
                                            break

                                        elif trial == 4:
                                            Error_message = f"Error in captcha. please check captcha_api.txt with correct key and token"
                                            print(f"unbale to load {Article_link}")
                                            error_list.append(Error_message)
                                            approach = False
                                            break

                        check_value, tpa_id = common_function.check_duplicate(DOI, Article_title, url_id, volume,
                                                                              issue)
                        if Check_duplicate.lower() == "true" and check_value:
                            message = f"{Article_link} - duplicate record with TPAID : {tpa_id}"
                            duplicate_list.append(message)
                            print("Duplicate Article :", Article_title)

                        else:
                            scrape_message = f"{Article_link}"
                            Pdf_link = f"https://www.pnas.org/doi/pdf/{DOI}"
                            try:
                                response = requests.get(Pdf_link, headers=headers)
                                if response.status_code != 200:
                                    response = requests.get(Pdf_link, proxies=get_random_proxy(), headers=headers)
                                    if response.status_code != 200:
                                        response = captcha_main.captcha_main(Pdf_link)
                                        if response.status_code != 200:
                                            Error_message = f"Error in captcha.failed to load {Pdf_link}"
                                            print("Retring.......")
                                            approach_2 = True
                                            trial_2 = 1
                                            while approach_2:
                                                time.sleep(random.randint(5, 10))
                                                response = get_request_article(Pdf_link)
                                                print("Retring.......")
                                                trial_2 = trial_2 + 1
                                                if response.status_code == 200:
                                                    approach_2 = False
                                                    break
                                                elif trial_2 == 4:
                                                    Error_message = f"Error in captcha. please check captcha_api.txt with correct key and token"
                                                    print(f"unbale to load {Pdf_link}")
                                                    error_list.append(Error_message)
                                                    approach = False
                                                    break

                                pdf_content = response.content
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
                                     "Special Issue": "", "Page Range": day, "Month": month,
                                     "Day": "",
                                     "Year": year,
                                     "URL": Article_link,
                                     "SOURCE File Name": f"{pdf_count}.pdf",
                                     "user_id": user_id})

                                df = pd.DataFrame(data)
                                df.to_excel(out_excel_file, index=False)
                                pdf_count += 1
                                completed_list.append(Article_link)

                                with open('completed.txt', 'a', encoding='utf-8') as write_file:
                                    write_file.write(Article_title + '\n')
                                print(
                                    f"The total number of PDFs {no_of_articles} , {status} PDF have been downloded...")
                                status += 1
                            except Exception as error:
                                Error_message = "Error in process :" + str(error)
                                print(Error_message)
                                error_list.append(Error_message)
                    try:
                        common_function.sendCountAsPost(url_id, Ref_value, str(no_of_articles), str(len(completed_list)),
                                                        str(len(duplicate_list)),
                                                        str(len(error_list)))
                    except Exception as error:
                        message = str(error)
                        print("New update")
                        error_list.append(message)
                    try:
                        if str(Email_Sent).lower() == "true":
                            attachment_path = out_excel_file
                            if os.path.isfile(attachment_path):
                                attachment = attachment_path
                            else:
                                attachment = None
                            common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                                 len(completed_list), ini_path, attachment, current_date,
                                                                 current_time, Ref_value)
                    except:
                        attachment_path = out_excel_file
                        if os.path.isfile(attachment_path):
                            attachment = attachment_path
                        else:
                            attachment = None
                        common_function.save_email_body(url_id, duplicate_list, error_list, completed_list,
                                                             len(completed_list), ini_path, attachment, current_date,
                                                             current_time, Ref_value,current_out)

                    sts_file_path = os.path.join(current_out, 'Completed.sts')
                    with open(sts_file_path, 'w') as sts_file:
                        pass
                except Exception as error:

                    Error_message = "Error in the site :" + str(error)
                    print(Error_message)
                    error_list.append(Error_message)
                    common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                         len(completed_list), ini_path, attachment, current_date,
                                                         current_time, Ref_value)
            except:
                pass
    except Exception as error:
        Error_message = "Error in the urls text file :" + str(error)
        print(Error_message)
        error_list.append(Error_message)
except:
    Error_message = "Error in the main process :"
    error_list.append(str(Error_message))
    log_file_path = os.path.join('log.txt')
    with open(log_file_path, 'w') as log_file:
        log_file.write(str(Error_message) + '\n')
















