import os
import re

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common_function
import pandas as pd
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver

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
options.add_argument('--user-agent=YOUR_USER_AGENT_STRING')
options.add_argument('--version_main=108')

driver = uc.Chrome(options=options)

def use_drive(url,request_cookies):
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

request_cookies = {
    'IWA_PublishingMachineID': '638491186796925668',
    '_ga': 'GA1.2.892686197.1713521884',
    '_gid': 'GA1.2.1313269268.1713521884',
    'fpestid': 'eh9u8XUlgdwuY7RUwBCYJv4NZVGOKeP548CWt1y_bFcLNWRt7tUehqHRQCwwsjI1bzLnNw',
    '_cc_id': 'c98eea9794bffe9e84dcd4916e261382',
    'panoramaId_expiry': '1714126683937',
    'panoramaId': '87bb27088c11dbcbf1612371515e16d53938c438922298f84a6f843eb4291467',
    'panoramaIdType': 'panoIndiv',
    'hum_iwap_visitor': '98fc3c8c-f2ea-4750-8fe8-42302f336a62',
    '__stripe_mid': 'debea6e4-2d7d-4d84-aeb3-37410dc7dbe192f50c',
    'IWA_SessionId': 'b0y5gtz4zk0y0gh5xrgouqwm',
    '__stripe_sid': 'f79e02a8-ef2f-4a96-9c7b-3381a4c74abd83cdba',
    '_gat_UA-10590794-3': '1',
    '_gat_UA-76340245-2': '1',
    '_ga_CY814T2KFP': 'GS1.2.1713550821.2.1.1713551342.60.0.0'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
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
    print(error)

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
        url, url_id = url_list[p].split(',')
        current_datetime = datetime.now()
        current_date = str(current_datetime.date())
        current_time = current_datetime.strftime("%H:%M:%S")

        ini_path = os.path.join(os.getcwd(), "Info.ini")
        Download_Path, Email_Sent, Check_duplicate, user_id = common_function.read_ini_file(ini_path)
        current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
        out_excel_file = common_function.output_excel_name(current_out)
        Ref_value = "49"

        if q == 0:
            print(url_id)

        duplicate_list = []
        error_list = []
        completed_list=[]
        data = []
        pdf_count = 1

        current_soup=use_drive(url,request_cookies)
        preVolume,preIssue=current_soup.find('div',class_='volume-issue__wrap').text.strip().split(', ')
        Volume=preVolume.split()[1]
        Issue=preIssue.split()[1]
        Day,Month,Year=current_soup.find('div',class_='ii-pub-date').text.strip().split()

        All_articles=current_soup.find('div',class_='section-container').findAll('div',class_='al-article-item-wrap al-normal')



        i, j = 0, 0
        while i < len(All_articles):

            Article_link,Article_title=None,None
            try:
                Article_link='https://iwaponline.com'+All_articles[i].find('h5',class_='item-title').find('a').get('href')
                Article_title = All_articles[i].find('h5',class_='item-title').text.strip()
                if not Article_link in read_content:
                    Article_details=use_drive(Article_link,request_cookies)
                    if Article_details.find('li',class_='toolbar-item item-pdf').find('a',class_='article-pdfLink'):
                        pdf_link='https://iwaponline.com'+Article_details.find('li',class_='toolbar-item item-pdf').find('a',class_='article-pdfLink').get('href')
                        DOI = Article_details.find('div', class_='citation-doi').text.strip().rsplit('doi.org/', 1)[-1]
                        Page_range = Article_details.find('div', class_='ww-citation-primary').text.strip().rsplit('): ', 1)[-1].rstrip('.')
                        check_value = common_function.check_duplicate(DOI, Article_title, url_id, Volume, Issue)
                        if Check_duplicate.lower()=="true" and check_value:
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
                            # get_driver_pdf(pdf_link, pdf_save, download_path,request_cookies)
                            pdf_content = requests.get(pdf_link, headers=headers).content
                            output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                            with open(output_fimeName, 'wb') as file:
                                file.write(pdf_content)
                            data.append(
                                {"Title": Article_title, "DOI": DOI, "Publisher Item Type": "", "ItemID": "",
                                 "Identifier": "",
                                 "Volume": Volume, "Issue": Issue, "Supplement": "", "Part": "",
                                 "Special Issue": "", "Page Range": Page_range, "Month": Month, "Day": Day,
                                 "Year": Year,
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






