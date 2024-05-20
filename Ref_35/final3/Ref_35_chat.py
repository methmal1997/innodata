import time
import captcha_main
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import common_function
import pandas as pd
import random
import re
import sys

# Suppress printing of errors
sys.tracebacklimit = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

duplicate_list = []
error_list = []
completed_list = []
attachment = None
url_id = None
current_date = None
current_time = None
Ref_value = None
ini_path = None

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


def get_random_proxy():
    return random.choice(formatted_proxies)


def get_soup(url):
    response = requests.get(url, headers=headers, timeout=20)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


try:
    with open('urlDetails.txt', 'r', encoding='utf-8') as file:
        url_list = file.read().split('\n')
    print("Process started...")
    print("This may take sometime. Please wait...")
    print("Urldetails text file was read...")
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

                duplicate_list = []
                error_list = []
                completed_list = []
                data = []
                pdf_count = 1
                Ref_value = "35"
                url_value = url.split('/')[-2]

                current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
                out_excel_file = common_function.output_excel_name(current_out)

                try:
                    try:
                        current_soup = get_soup(url)
                        current_issue = current_soup.find('div', class_='view-current-issue')
                        current_issue_link = current_soup.find('div', class_='view-current-issue').find('a').get(
                            'href')

                    except Exception:
                        print("Normal request failed")
                        proxy_number = 0
                        proxy_failed = True
                        while proxy_number < 10:
                            try:
                                print("trying proxy...: ", proxy_number)
                                response = requests.get(url, proxies=formatted_proxies[proxy_number],
                                                        headers=headers, timeout=20)
                                response_2 = requests.get('https://api.ipify.org?format=json',
                                                          proxies=formatted_proxies[proxy_number], headers=headers,
                                                          timeout=20)
                                proxy_ip = response_2.json()['ip']
                                print('Proxy IP:', proxy_ip)
                                current_soup = BeautifulSoup(response.content, 'html.parser')
                                current_issue = current_soup.find('div', class_='view-current-issue')
                                current_issue_link = current_soup.find('div', class_='view-current-issue').find(
                                    'a').get('href')
                                proxy_failed = False
                                break
                            except Exception:
                                proxy_number += 1

                        if proxy_failed:
                            try:
                                print("Proxy failed. trying captcha solver...")
                                time.sleep(random.randint(5, 9))
                                response = captcha_main.captcha_main(url)
                                current_soup = BeautifulSoup(response.content, 'html.parser')
                                current_issue = current_soup.find('div', class_='view-current-issue')
                                current_issue_link = current_soup.find('div', class_='view-current-issue').find(
                                    'a').get('href')
                            except Exception as error:
                                Error_message = "Error in captcha. please check captcha_api.txt with correct key and token :" + str(
                                    error)
                                print(Error_message)

                    current_issue_link = 'https://journals.biologists.com/' + current_issue_link

                    try:
                        try:
                            response = requests.get(current_issue_link, headers=headers, timeout=20)
                            current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                            volume_issue = current_soup_2.find('span', class_='volume issue').text.split(', ')
                        except Exception:
                            response = requests.get(current_issue_link, proxies=formatted_proxies[proxy_number],
                                                    headers=headers, timeout=20)
                            current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                            volume_issue = current_soup_2.find('span', class_='volume issue').text.split(', ')
                    except Exception:
                        try:
                            response = captcha_main.captcha_main(current_issue_link)
                        except Exception as error:
                            Error_message = "Error in captcha. please check captcha_api.txt with correct key and token :" + str(
                                error)
                            print(Error_message)
                            error_list.append(Error_message)

                    if response.status_code == 200:
                        current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                        volume_issue = current_soup_2.find('span', class_='volume issue').text.split(', ')
                        volume = volume_issue[0].split()[1]
                        issue = volume_issue[1].split()[1]
                        date = current_soup_2.find('div', class_='ii-pub-date').text.split()
                        month = date[0]
                        year = date[1]

                        articles_count = len(current_soup_2.find_all('div', class_='al-article-items'))
                        articles_count_with_pdf = current_soup_2.find_all('a',
                                                                          class_='al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink')
                        articles_count_with_pdf = len(articles_count_with_pdf)
                        status = 0
                        print("Number of articles : ", articles_count)
                        print("Number of articles with PDF : ", articles_count_with_pdf)

                        article_sections = current_soup_2.find_all('div', class_='al-article-items')
                        for section in article_sections:
                            Article_title = str(section.find('h5', class_="customLink item-title").text).strip()
                            reasearch_link = section.find('a',
                                                          class_='al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink')

                            if not Article_title in read_content:

                                Article_link = 'https://journals.biologists.com' + section.find('h5',
                                                                                                class_="customLink item-title").find(
                                    'a').get('href')
                                try:
                                    Pdf_link = "https://journals.biologists.com" + reasearch_link.get(
                                        'href')
                                    Pdf_link = captcha_main.current_url(Pdf_link)

                                    try:
                                        response = requests.get(Article_link, headers=headers, timeout=20)
                                        current_soup_pdf = BeautifulSoup(response.content,
                                                                         'html.parser')
                                        current_soup_pdf.find('h1',
                                                              class_='wi-article-title article-title-main').text

                                    except Exception:
                                        response = requests.get(Article_link, proxies=formatted_proxies[proxy_number],
                                                                headers=headers, timeout=20)
                                        current_soup_pdf = BeautifulSoup(response.content,
                                                                         'html.parser')
                                        current_soup_pdf.find('h1',
                                                              class_='wi-article-title article-title-main').text
                                    except Exception:
                                        response = captcha_main.captcha_main(Article_link)
                                        current_soup_pdf = BeautifulSoup(response.content,
                                                                         'html.parser')

                                    try:
                                        DOI = current_soup_pdf.find('div', class_='citation-doi').text
                                        DOI = re.search(r'(?<=\bdoi.org\/)\d+\.\d+\/\w+.\d+', DOI).group(0)
                                    except:
                                        DOI = ''

                                    check_value = common_function.check_duplicate(DOI, Article_title,
                                                                                  url_id, volume,
                                                                                  issue)
                                    try:
                                        if Check_duplicate.lower() == "true" and check_value:
                                            message = f"{Article_link} - duplicate record with TPAID {{tpaid returned in response}}"
                                            duplicate_list.append(message)
                                            print("Duplicate Article :", Article_title)

                                        else:

                                            try:

                                                response = requests.get(Pdf_link, headers=headers, timeout=20)
                                                if "We are sorry, but we are experiencing unusual traffic at this time. Please help us confirm that you are not a robot and we will take you to your content" in response.text:
                                                    response = captcha_main.captcha_main(Pdf_link)
                                                    pdf_content = response.content

                                                else:
                                                    pdf_content = response.content
                                            except Exception:
                                                try:
                                                    response = captcha_main.captcha_main(Pdf_link)
                                                    pdf_content = response.content
                                                except Exception:
                                                    try:
                                                        time.sleep(3)
                                                        response = captcha_main.captcha_main(Pdf_link)
                                                        pdf_content = response.content
                                                    except Exception:
                                                        Error_message = "Failed to navigate to the link.captcha error..."
                                                        print(Error_message)
                                                        error_list.append(Error_message)

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
                                                 "Special Issue": "", "Page Range": "", "Month": month,
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
                                            status += 1
                                            print(
                                                f"The total number of PDFs {articles_count_with_pdf} , {status} PDF have been downloded...")
                                            print("###########")
                                    except Exception as error:
                                        if not status == articles_count_with_pdf:
                                            Error_message = "Error in process :" + str(error)
                                            print(Error_message)
                                            error_list.append(Error_message)
                                        else:
                                            print("Next URL..")

                                except Exception:
                                    pass

                            else:
                                status += 1
                                print("Already downloaded PDF. Skipped..")
                                print(
                                    f"The total number of PDFs {articles_count_with_pdf} , {status} PDF have been downloaded.")
                                print("###########")

                    # Email sending
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
                    except Exception:

                        attachment_path = out_excel_file
                        if os.path.isfile(attachment_path):
                            attachment = attachment_path
                        else:
                            attachment = None

                        common_function.save_email_body(url_id, duplicate_list, error_list, completed_list,
                                                             len(completed_list), ini_path, attachment, current_date,
                                                             current_time, Ref_value, current_out)

                    sts_file_path = os.path.join(current_out, 'Completed.sts')
                    with open(sts_file_path, 'w'):
                        pass
                    time.sleep(10)
                except Exception as error:
                    Error_message = "Error in the site :" + str(error)
                    print(Error_message)
                    error_list.append(Error_message)
                    common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                         len(completed_list), ini_path, attachment, current_date,
                                                         current_time, Ref_value)
                time.sleep(random.randint(5, 9))

            except Exception as error:
                Error_message = "Error in the urls text file :" + str(error)
                print(Error_message)
                error_list.append(Error_message)
        except Exception:
            pass

except Exception:
    Error_message = "Error in the main process :"
    error_list.append(str(Error_message))
    log_file_path = os.path.join('log.txt')
    with open(log_file_path, 'w'):
        pass

input("Download finished. Press Enter to exit...")
