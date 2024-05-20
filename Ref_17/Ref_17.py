import time

import requests
from bs4 import BeautifulSoup
import os
import re
import common_function
from datetime import datetime
import pandas as pd
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver.install()

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
driver = uc.Chrome(options=options)

def use_drive(url,request_cookies):
    driver.get(url)
    time.sleep(2)
    driver.get(url)
    for cookie_name, cookie_value in request_cookies.items():
        driver.add_cookie({"name": cookie_name, "value": cookie_value})

    driver.get(url)
    content = driver.page_source
    uc_soup = BeautifulSoup(content, 'html.parser')
    return uc_soup

def get_cookies():
    cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])
    return cookies

request_cookies={
    'GeoScienceWorldMachineID': '638475566012738969',
    'fpestid': 'f6tdgLTO5-uu-D79o3BwgcCJ8LIF5rYe6uzYtjoq9QujxAeEBDCLFb5WQ0DZ1DA7wo7mWA',
    '_ga': 'GA1.1.1487530923.1711959819',
    '_gid': 'GA1.3.569889817.1711959819',
    '_cc_id': '23c309b2b916c241c5354943d7a590ab',
    'panoramaId_expiry': '1712564622863',
    'panoramaId': '0a62239d6889f74214825d16dbaf185ca02cf678ef814ebd2813a55b670875f8',
    'panoramaIdType': 'panoDevice',
    '_hjSessionUser_2619384': 'eyJpZCI6ImM4ZTc4YjNmLTIzYmItNTkyMi1iZDcwLWY5YzFmNWMyMzQyZSIsImNyZWF0ZWQiOjE3MTE5NTk4MjU0NzYsImV4aXN0aW5nIjp0cnVlfQ==',
    'hubspotutk': '31fbd733f95a4abb67792c123cf2d8b4',
    'GDPR_24_.geoscienceworld.org': 'true',
    'TheDonBot': 'D47BD6096350C06E91E5E85FFD4A95DF',
    'GSW_SessionId': 'gyjp0c2zr4to30bzz5irddko',
    '_gat_UA-28112735-4': '1',
    '_gat_UA-28112735-1': '1',
    '_gat_UA-50143594-1': '1',
    '_gat_UA-28112735-5': '1',
    '_gat_UA-76340245-2': '1',
    '_gat_UA-1008571-9': '1',
    '_gat_UA-1008571-10': '1',
    '_gat_UA-1008571-11': '1',
    '_gat_UA-1008571-12': '1',
    '_gat_UA-1008571-15': '1',
    '_gat_UA-1008571-16': '1',
    '_gat_UA-1008571-17': '1',
    '_gat_UA-1008571-18': '1',
    '_ga_YVB7JQBY6Z': 'GS1.1.1711999347.5.0.1711999347.0.0.0',
    '_hjSession_2619384': 'eyJpZCI6IjNmMWM2NWVkLTY4OTEtNDliOS1hNDFhLTVkYTNkNGI5M2Q0NyIsImMiOjE3MTE5OTkzNDc5MDEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    '_ga_11RK1D9N56': 'GS1.3.1711999348.5.0.1711999348.0.0.0',
    '_ga_MKZCHDYBTN': 'GS1.3.1711999348.5.0.1711999348.0.0.0',
    '_ga_781B8JFM4R': 'GS1.3.1711999348.5.0.1711999348.0.0.0',
    '_ga_KZ8XM8M5S3': 'GS1.3.1711999348.5.0.1711999348.0.0.0',
    '_ga_5FBFHZKYCW': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_YY6XD0X474': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_RBDZFVMYBJ': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_LK2NSTY4C0': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_2ZJXB7SCK6': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_HP48M3E3R7': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '__hstc': '147277928.31fbd733f95a4abb67792c123cf2d8b4.1711959837613.1711973459982.1711999352182.5',
    '__hssrc': '1',
    '__hssc': '147277928.1.1711999352182'
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
    with open('urlDetails.txt','r',encoding='utf-8') as file:
        url_list=file.read().split('\n')
except Exception as error:
    Error_message = "Error in the urlDetails text file :" + str(error)
    print(Error_message)
    error_list.append(Error_message)
    common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list, len(completed_list),
                                         ini_path, attachment, current_date, current_time, Ref_value)

try:
    with open('completed.txt', 'r', encoding='utf-8') as read_file:
        read_content = read_file.read().split('\n')
except FileNotFoundError:
    with open('completed.txt', 'w', encoding='utf-8'):
        with open('completed.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().split('\n')

p, q = 0, 0
while p < len(url_list):
    try:
        url,url_id=url_list[p].split(',')
        data = []
        duplicate_list = []
        error_list = []
        completed_list=[]
        pdf_count=1

        current_datetime = datetime.now()
        current_date = str(current_datetime.date())
        current_time = current_datetime.strftime("%H:%M:%S")

        ini_path = os.path.join(os.getcwd(), "Info.ini")
        Download_Path, Email_Sent, Check_duplicate, user_id = common_function.read_ini_file(ini_path)
        current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
        out_excel_file = common_function.output_excel_name(current_out)
        Ref_value = "17"
        print(url_id)

        soup = use_drive(url,request_cookies)
        Volume = re.sub(r'[^0-9]+', "", soup.find('span', class_='volume issue').text.strip().split(',')[0])
        Issue = re.sub(r'[^0-9]+', "", soup.find('span', class_='volume issue').text.strip().split(',')[1])
        Month,Year = soup.find('div', class_='ii-pub-date').text.strip().split(' ')
        All_articles = soup.find('div',class_='section-container').findAll('div', class_='al-article-item-wrap al-normal')
        i, j = 0, 0
        while i < len(All_articles):
            Article_link,Article_title=None,None
            try:
                Article_title = All_articles[i].find('h5', class_='item-title').find('a').text.strip()
                Article_link = "https://pubs.geoscienceworld.org" + All_articles[i].find('h5', class_='item-title').find('a').get('href')
                if not Article_link in read_content:
                    Page_range_doi = All_articles[i].find('div', class_='al-cite-description').text.strip()
                    Page_range =  ((re.compile(r'Vol\.(.*?)doi', re.DOTALL).search(Page_range_doi)).group(1)
                                       .strip().rstrip('.').split(',')[-1].strip())
                    DOI=Page_range_doi.rsplit('doi.org/',1)[-1]
                    Article_details = use_drive("https://pubs.geoscienceworld.org" + All_articles[i].find('h5', class_='item-title').find('a').get('href'),request_cookies)
                    pdf_link_check=Article_details.find('ul',class_='debug js-toolbar toolbar')
                    pdf_link='https://pubs.geoscienceworld.org'+pdf_link_check.find('li', class_='item-pdf').find('a').get('href')
                    check_value = common_function.check_duplicate(DOI, Article_title, url_id, Volume, Issue)
                    if Check_duplicate.lower() == "true" and check_value:
                        message = f"{Article_link} - duplicate record with TPAID {{tpaid returned in response}}"
                        duplicate_list.append(message)
                        print("Duplicate Article :", Article_title)
                    else:
                        cookies = get_cookies()
                        headers = {
                            "Cookie": f"{cookies}",
                            # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
                            'User-Agent': 'YOUR_USER_AGENT_STRING'
                        }
                        pdf_content = requests.get(pdf_link,headers=headers).content
                        output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                        with open(output_fimeName, 'wb') as file:
                            file.write(pdf_content)
                        data.append(
                            {"Title": Article_title, "DOI": DOI, "Publisher Item Type": "", "ItemID": "", "Identifier": "",
                             "Volume": Volume, "Issue": Issue, "Supplement": "", "Part": "",
                             "Special Issue": "", "Page Range": Page_range, "Month": "", "Day": "", "Year": "",
                             "URL": pdf_link, "SOURCE File Name": f"{pdf_count}.pdf", "user_id": user_id})
                        df = pd.DataFrame(data)
                        df.to_excel(out_excel_file, index=False)
                        pdf_count += 1
                        scrape_message = f"{Article_link}"
                        completed_list.append(scrape_message)
                        with open('completed.txt', 'a', encoding='utf-8') as write_file:
                            write_file.write(Article_link + '\n')
                        print("Original Article :", Article_title)
                else:
                    print("Already downloaded article :", Article_title)
                i, j = i + 1, 0
            except Exception as error:
                if j < 4:
                    j += 1
                else:
                    message=f"Error link - {Article_link} : {str(error)}"
                    print("Download failed :",Article_title)
                    error_list.append(message)
                    i, j = i + 1, 0

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
        p, q = p + 1, 0
    except Exception as error:
        if q < 4:
            q += 1
        else:
            Error_message = "Error in the driver :" + str(error)
            print("Error in the driver or site")
            error_list.append(Error_message)
            common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                 len(completed_list),
                                                 ini_path, attachment, current_date, current_time, Ref_value)
            p, q = p + 1, 0

driver.quit()









