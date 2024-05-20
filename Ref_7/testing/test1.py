import random
import time
import requests
from bs4 import BeautifulSoup
import os
import re
import common_function
from datetime import datetime
import pandas as pd
import undetected_chromedriver as uc
import captcha_main

print("This is Ref_7")

duplicate_list = []
error_list = []
completed_list = []
attachment = None
url_id = None
current_date = None
current_time = None
Ref_value = None
ini_path = None

options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--user-agent=YOUR_USER_AGENT_STRING')
options.add_argument('--version_main=108')
driver = uc.Chrome(options=options)

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

def get_current_cookies(url):
    driver.delete_all_cookies()
    driver.get(url)
    time.sleep(random.uniform(0, 3))
    selenium_cookies = driver.get_cookies()
    cookies_for_requests = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
    return cookies_for_requests

def go_into_article(url):
    response = None
    try:
        try:
            print("article_1.1 ")
            response = requests.get(url, headers=headers, timeout=20,
                                    cookies=get_current_cookies(url))
            current_soup_2 = BeautifulSoup(response.content, 'html.parser')

            try_catch = current_soup_2.find('div', class_='ww-citation-wrap-doi').find('a').text.strip().rsplit('doi.org/', 1)[-1].rstrip(
                '.')
            print("article_1.2 - normal request succeed")
        except:
            print("article_2.2 - normal request failed. trying proxy..")
            proxy_number = 0
            proxy_failed = True
            while proxy_failed:

                if proxy_number < 3:
                    try:
                        print("trying proxy...: ", proxy_number)
                        response = requests.get(url, proxies=formatted_proxies[proxy_number],
                                                headers=headers, timeout=20,
                                                cookies=get_current_cookies(url))
                        response_2 = requests.get('https://api.ipify.org?format=json',
                                                  proxies=formatted_proxies[proxy_number],
                                                  headers=headers,
                                                  timeout=20)
                        proxy_ip = response_2.json()['ip']
                        print('Proxy IP:', proxy_ip)
                        current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                        try_catch = current_soup_2.find('div', class_='ww-citation-wrap-doi').find('a').text.strip().rsplit('doi.org/', 1)[-1].rstrip('.')
                        print("article_2.2  - proxy request succeed")
                        proxy_failed = False

                        break
                    except:
                        proxy_number = proxy_number + 1
                else:
                    try_catch = \
                    current_soup_2.find('div', class_='ww-citation-wrap-doi').find('a').text.strip().rsplit('doi.org/',
                                                                                                            1)[
                        -1].rstrip('.')
                    break

    except:
        try:
            print("article_3.1 proxy failed. trying 2captcha..")
            time.sleep(random.randint(5, 9))
            response = captcha_main.captcha_main(current_issue_link)
            current_soup_2 = BeautifulSoup(response.content, 'html.parser')
            try_catch = current_soup_2.find('div', class_='ww-citation-wrap-doi').find('a').text.strip().rsplit('doi.org/', 1)[-1].rstrip('.')
            print("article_3.2  - 2captcha request succeed")
        except Exception as error:
            print("Retring captcha - article_loading")
            trial_0 = 1
            approach_0 = True
            while approach_0:
                time.sleep(random.randint(5, 10))
                response = captcha_main.captcha_main(url)
                print(f"Retring captcha article_loading - {trial_0}")
                trial_0 = trial_0 + 1
                if response.status_code == 200 and trial_0 < 11:
                    try:
                        print(f"Retrying 2captcha trial - {trial_0}")
                        current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                        try_catch = current_soup_2.find('div', class_='ww-citation-wrap-doi').find('a').text.strip().rsplit('doi.org/', 1)[-1].rstrip('.')
                        approach_0 = False
                        print(f"article_3.2  - captcha request succeed - trial {trial_0}")
                        break
                    except:
                        pass
                elif trial_0 == 10:
                    Error_message = f"article_loading- Normal request failed. proxy failed. Error in captcha. please check captcha_api.txt with correct key and token"
                    error_list.append(Error_message)
                    print(Error_message)
                    response = None
                    approach = False
                    break

    return response


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

                duplicate_list = []
                error_list = []
                completed_list = []
                data = []
                pdf_count = 1
                Ref_value = "7"
                url_value = url.split('/')[-2]

                current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
                out_excel_file = common_function.output_excel_name(current_out)

                try:
                    try:
                        response = requests.get(url, headers=headers, timeout=20, cookies=get_current_cookies(url))
                        current_soup = BeautifulSoup(response.content, 'html.parser')
                        current_soup_1 = current_soup.find('div', class_='article-issue-info')
                        Volume = re.sub(r'[^0-9]+', "", current_soup_1.find('div', class_='volume').text.strip())
                        Issue = re.sub(r'[^0-9]+', "", current_soup_1.find('div', class_='issue').text.strip())
                        Date, Month, Year = current_soup_1.find('div', class_='ii-pub-date').text.strip().split(' ')
                    except:
                        print("Normal request failed")
                        proxy_number = 0
                        proxy_failed = True

                        while proxy_failed:

                            if proxy_number < 3:
                                try:
                                    print("trying proxy...: ", proxy_number)
                                    response = requests.get(url, proxies=formatted_proxies[proxy_number],
                                                            headers=headers, timeout=20,cookies=get_current_cookies(url))
                                    response_2 = requests.get('https://api.ipify.org?format=json',
                                                              proxies=formatted_proxies[proxy_number], headers=headers,
                                                              timeout=20)
                                    proxy_ip = response_2.json()['ip']
                                    print('Proxy IP:', proxy_ip)
                                    current_soup = BeautifulSoup(response.content, 'html.parser')
                                    current_soup_1 = current_soup.find('div', class_='article-issue-info')
                                    Volume = re.sub(r'[^0-9]+', "",
                                                    current_soup_1.find('div', class_='volume').text.strip())
                                    Issue = re.sub(r'[^0-9]+', "",
                                                   current_soup_1.find('div', class_='issue').text.strip())
                                    Date, Month, Year = current_soup_1.find('div',
                                                                            class_='ii-pub-date').text.strip().split(' ')
                                    proxy_failed = False
                                    break
                                except:
                                    proxy_number = proxy_number + 1
                            else:
                                break

                        if proxy_failed:
                            try:
                                print("Proxy failed. trying captcha slover...")
                                time.sleep(random.randint(5, 9))
                                response = captcha_main.captcha_main(url)
                                current_soup = BeautifulSoup(response.content, 'html.parser')
                                current_soup_1 = current_soup.find('div', class_='article-issue-info')
                                Volume = re.sub(r'[^0-9]+', "",
                                                current_soup_1.find('div', class_='volume').text.strip())
                                Issue = re.sub(r'[^0-9]+', "",
                                               current_soup_1.find('div', class_='issue').text.strip())
                                Date, Month, Year = current_soup_1.find('div',
                                                                        class_='ii-pub-date').text.strip().split(' ')
                            except Exception as error:
                                Error_message = f"Error in captcha."
                                print(Error_message)
                                print("Retring.......")
                                trial_0 = 1
                                approach_0 = True
                                while approach_0:
                                    time.sleep(random.randint(5, 10))
                                    response = captcha_main.captcha_main(url)
                                    print("Retring.......")
                                    trial_0 = trial_0 + 1
                                    if response.status_code == 200 and trial_0<11:
                                        try:
                                            print(f"Retrying 2captcha trial - {trial_0}")
                                            current_soup = BeautifulSoup(response.content, 'html.parser')
                                            current_soup_1 = current_soup.find('div', class_='article-issue-info')
                                            Volume = re.sub(r'[^0-9]+', "",
                                                            current_soup_1.find('div', class_='volume').text.strip())
                                            Issue = re.sub(r'[^0-9]+', "",
                                                           current_soup_1.find('div', class_='issue').text.strip())
                                            Date, Month, Year = current_soup_1.find('div',
                                                                                    class_='ii-pub-date').text.strip().split(
                                                ' ')
                                            approach_0 = False
                                            break
                                        except:
                                            pass
                                    elif trial_0 == 10:
                                        Error_message = f"Normal request failed. proxy failed. Error in captcha. please check captcha_api.txt with correct key and token"
                                        error_list.append(Error_message)
                                        print(Error_message)
                                        approach = False
                                        break

                    print(Date)
                    print(Month)
                    print(Year)
                    current_issue_link =  'https://journals.aai.org'+current_soup_1.find('div',class_='view-current-issue').find('a')['href']

                    try:
                        try:
                            print("trt_1.1 ")
                            response = requests.get(current_issue_link, headers=headers, timeout=20,cookies = get_current_cookies(current_issue_link))
                            current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                            try_catch = current_soup_2.find('div',
                                                                class_='issue-browse-top issue-browse-mobile-nav').text
                            print("trt_1.2 - normal request succeed")
                        except:
                            print("trt_2.1 ")
                            proxy_number = 0
                            proxy_failed = True
                            while proxy_failed:
                                if proxy_number < 3:
                                    try:
                                        print("trying proxy...: ", proxy_number)
                                        response = requests.get(current_issue_link, proxies=formatted_proxies[proxy_number],
                                                                headers=headers, timeout=20,
                                                                cookies=get_current_cookies(current_issue_link))
                                        response_2 = requests.get('https://api.ipify.org?format=json',
                                                                  proxies=formatted_proxies[proxy_number],
                                                                  headers=headers,
                                                                  timeout=20)
                                        proxy_ip = response_2.json()['ip']
                                        print('Proxy IP:', proxy_ip)
                                        current_soup_2= BeautifulSoup(response.content, 'html.parser')
                                        try_catch = current_soup_2.find_all('div',
                                                                            class_='issue-browse-top issue-browse-mobile-nav').text
                                        print("trt_2.2 - proxy request succeed")
                                        proxy_failed = False

                                        break
                                    except:
                                        proxy_number = proxy_number + 1
                                else:
                                    try_catch = current_soup_2.find_all('div',
                                                                        class_='issue-browse-top issue-browse-mobile-nav').text
                                    break

                    except:
                        try:
                            print("trt_3.1")
                            time.sleep(random.randint(5, 9))
                            response = captcha_main.captcha_main(current_issue_link)
                            current_soup_2 = BeautifulSoup(response.content, 'html.parser')
                            try_catch = current_soup_2.find_all('div',
                                                                class_='issue-browse-top issue-browse-mobile-nav')
                            print("trt_3.2 - 2captcha request succeed")
                        except Exception as error:

                            Error_message = f"Error in captcha. current_issue_link"
                            print(Error_message)
                            print("Retring captcha - current_issue_link")
                            trial_0 = 1
                            approach_0 = True
                            while approach_0:
                                time.sleep(random.randint(5, 10))
                                response = captcha_main.captcha_main(url)
                                print(f"Retring captcha current_issue_link - {trial_0}")
                                trial_0 = trial_0 + 1
                                if response.status_code == 200 and trial_0 < 11:
                                    try:
                                        print(f"Retrying 2captcha trial - {trial_0}")
                                        current_soup = BeautifulSoup(response.content, 'html.parser')
                                        current_soup_1 = current_soup.find('div', class_='article-issue-info')
                                        Volume = re.sub(r'[^0-9]+', "",
                                                        current_soup_1.find('div', class_='volume').text.strip())
                                        Issue = re.sub(r'[^0-9]+', "",
                                                       current_soup_1.find('div', class_='issue').text.strip())
                                        Date, Month, Year = current_soup_1.find('div',
                                                                                class_='ii-pub-date').text.strip().split(
                                            ' ')
                                        approach_0 = False
                                        print(f"trt_3.2 - captcha request succeed - trial {trial_0}")
                                        break
                                    except:
                                        pass
                                elif trial_0 == 10:
                                    Error_message = f"cuurent issue- Normal request failed. proxy failed. Error in captcha. please check captcha_api.txt with correct key and token"
                                    error_list.append(Error_message)
                                    print(Error_message)
                                    approach = False
                                    break

                    All_article = current_soup_2.find_all('div',class_ = "al-article-item-wrap al-normal")
                    articles_count_with_pdf = len(All_article)
                    status_pdf = 0
                    print("Number of articles with PDF: ", articles_count_with_pdf)

                    try:

                        for article in All_article:
                            Article_title = article.find('h5', class_='item-title').find('a').text.strip()
                            if not Article_title in read_content:
                                Article_link = "https://journals.aai.org" + article.find('h5', class_='item-title').find(
                                    'a').get('href')
                                Page_range = article.find('div', class_='ww-citation-primary').text.strip().rsplit('): ', 1)[-1].rstrip('.')
                                pdf_link = "https://journals.aai.org/"+article.find('a',class_='al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink')['href']
                                pdf_link = captcha_main.current_url(pdf_link)
                                article_response = go_into_article(Article_link)
                                article = BeautifulSoup(article_response.content, 'html.parser')
                                DOI = article.find('div', class_='ww-citation-wrap-doi').find('a').text.strip().rsplit('doi.org/',1)[-1].rstrip('.')
                                check_value = common_function.check_duplicate(DOI, Article_title, url_id, Volume, Issue)
                                if Check_duplicate.lower() == "true" and check_value:
                                    message = f"{Article_title} - duplicate record with TPAID {{tpaid returned in response}}"
                                    duplicate_list.append(message)
                                    print("Duplicate Article :", Article_title)

                                else:
                                    print("pdf_1.1 ")
                                    status = True
                                    pdf_trail = 1
                                    while status:
                                        time.sleep(random.uniform(5, 10))
                                        response = requests.get(pdf_link, headers=headers, timeout=20,cookies=get_current_cookies(pdf_link),allow_redirects=True)
                                        if response.status_code == 200 and pdf_trail<3:
                                            print("pdf_1.2 - normal request succeed")
                                            break
                                        elif pdf_trail == 10:
                                            break
                                        pdf_trail = pdf_trail + 1
                                    if response != 200:
                                        proxy_number = 0
                                        proxy_failed = True
                                        print("pdf_2.1")
                                        while proxy_failed:
                                            if proxy_number < 3:

                                                print("trying proxy...: ", proxy_number)
                                                response = requests.get(pdf_link,
                                                                        proxies=formatted_proxies[proxy_number],
                                                                        headers=headers, timeout=20,
                                                                        cookies=get_current_cookies(current_issue_link),allow_redirects=True)
                                                response_2 = requests.get('https://api.ipify.org?format=json',
                                                                          proxies=formatted_proxies[proxy_number],
                                                                          headers=headers,
                                                                          timeout=20)
                                                proxy_ip = response_2.json()['ip']
                                                print('Proxy IP:', proxy_ip)
                                                if response.status_code == 200 or proxy_number < 10:
                                                    print("pdf_2.2 - normal request succeed")
                                                    break
                                                proxy_number = proxy_number + 1
                                            else:
                                                break

                                    if response != 200:
                                        print("pdf_3.1")
                                        response = captcha_main.captcha_main(pdf_link)
                                        if not response != 200:
                                            print("Retrying captcha")
                                            trial_0 = 1
                                            approach_0 = True
                                            while approach_0:
                                                time.sleep(random.randint(5, 10))
                                                response = captcha_main.captcha_main(pdf_link)
                                                print(f"Retring captcha {trial_0}")
                                                if response.status_code == 200 or trial_0 < 11:
                                                    print("pdf_3.2 - captcha request succeed")
                                                    break
                                                trial_0 = trial_0 + 1
                                    pdf_content = response.content
                                    output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                                    with open(output_fimeName, 'wb') as file:
                                        file.write(pdf_content)
                                    data.append(
                                        {"Title": Article_title, "DOI": DOI, "Publisher Item Type": "", "ItemID": "",
                                         "Identifier": "",
                                         "Volume": Volume, "Issue": Issue, "Supplement": "", "Part": "",
                                         "Special Issue": "", "Page Range": Page_range, "Month": Month, "Day": "",
                                         "Year": Year,
                                         "URL": pdf_link, "SOURCE File Name": f"{pdf_count}.pdf", "user_id": user_id})
                                    df = pd.DataFrame(data)
                                    df.to_excel(out_excel_file, index=False)
                                    pdf_count += 1
                                    scrape_message = f"{Article_title}"
                                    completed_list.append(scrape_message)
                                    with open('completed.txt', 'a', encoding='utf-8') as write_file:
                                        write_file.write(Article_title + '\n')
                                    print(Article_title)
                                    status_pdf += 1
                                    print(
                                        f"The total number of PDFs {articles_count_with_pdf} , {status_pdf} PDF have been downloded...")
                                    print("###########")

                            else:
                                    status_pdf += 1
                                    print(Article_title)
                                    print("Already downloded PDF. Skipped..")
                                    print(
                                        f"The total number of PDFs {articles_count_with_pdf} , {status_pdf} PDF have been downloded.")
                                    print("###########")
                    except:
                        Error_message = "Error in scraping process or dataframe creation :" + str(error)
                        print(Error_message)
                        error_list.append(Error_message)

                    # Email sending
                    print("check point 1")
                    try:
                        print("check point 2")
                        if str(Email_Sent).lower() == "true":
                            attachment_path = out_excel_file
                            if os.path.isfile(attachment_path):
                                attachment = attachment_path
                            else:
                                attachment = None
                            common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                                 len(completed_list), ini_path, attachment,
                                                                 current_date,
                                                                 current_time, Ref_value)
                        print("check point 3")
                    except:
                        print("check point 4")
                        attachment_path = out_excel_file
                        if os.path.isfile(attachment_path):
                            attachment = attachment_path
                        else:
                            attachment = None

                        common_function.save_email_body(url_id, duplicate_list, error_list, completed_list,
                                                        len(completed_list), ini_path, attachment, current_date,
                                                        current_time, Ref_value, current_out)
                        print("In local machine email body will be saved")
                        print("check point 5")

                    sts_file_path = os.path.join(current_out, 'Completed.sts')
                    with open(sts_file_path, 'w') as sts_file:
                        pass
                    time.sleep(10)
                    print("check point 6")


                except Exception as error:
                    try:
                        print("check point 7")
                        Error_message = "Error in the site :" + str(error)
                        print(Error_message)
                        error_list.append(Error_message)
                        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                             len(completed_list), ini_path, attachment, current_date,
                                                             current_time, Ref_value)
                        print("check point 8")
                    except:
                        print("check point 9")
                        Error_message = "Error in the site :" + str(error)
                        print(Error_message)
                        error_list.append(Error_message)
                        common_function.save_email_body(url_id, duplicate_list, error_list, completed_list,
                                                        len(completed_list), ini_path, attachment, current_date,
                                                        current_time, Ref_value, current_out)
                time.sleep(random.randint(5, 9))

            except Exception as error:
                Error_message = "Error in the urls text file :" + str(error)
                print(Error_message)
                error_list.append(Error_message)

        except:
            pass
except:
    Error_message = "Error in the main process :"

    error_list.append(str(Error_message))
    log_file_path = os.path.join('log.txt')
    with open(log_file_path, 'w') as log_file:
        log_file.write(str(Error_message) + '\n')

input("Download finished. Press Enter to exit...")








