import re
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import common_function
import pandas as pd
import time
import undetected_chromedriver as uc
import chromedriver-autoinstaller as chromedriver

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

request_cookies={
    'TheDonBot': 'F4DFB633CFB6BDC35D512115B26E718D',
    'The_Company_of_BiologistsMachineID': '638470805314470355',
    '__gads': 'ID=9c63c54c3d2f2918:T=1711483734:RT=1711483734:S=ALNI_MYEqdeMOgvv-9ecOaoaGJY_nIdUqw',
    '__gpi': 'UID=00000d67b069a251:T=1711483734:RT=1711483734:S=ALNI_MZRO8BRpNRDooW-LPeNvTi0C57XDA',
    '__eoi': 'ID=0182cd1d86221541:T=1711483734:RT=1711483734:S=AA-AfjZGRVwjlRkBIG0zmepsESmo',
    'fpestid': 'NbrMapwGCeKuWDGaAm9kIoh3eRZUatLUtIfVECqtWhNFEemEUc-2vDmbmQDL3XaklelMpg',
    '__stripe_mid': 'bb9bbc44-7059-48a3-a9c3-40d54e7d9ec29e80d8',
    '_cc_id': '23c309b2b916c241c5354943d7a590ab',
    'panoramaId_expiry': '1712088535625',
    'panoramaId': 'f172d411e6629317a72b7b3d0265185ca02cd0398a246c61e4507a03ae330588',
    'panoramaIdType': 'panoDevice',
    'OptanonAlertBoxClosed': '2024-03-26T20:08:54.531Z',
    '_gid': 'GA1.2.221090924.1711970078',
    '_ga_G5TCNFJCYP': 'GS1.1.1711974217.1.0.1711974217.0.0.0',
    'COB_SessionId': 'u2hjclyajcwfn23321ckiuy2',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Apr+02+2024+09%3A01%3A07+GMT%2B0530+(India+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=8634e824-de47-4598-b076-193bbd3487e2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0001%3A1&geolocation=LK%3B1&AwaitingReconsent=false',
    '__stripe_sid': '8799ce92-00a5-4d2a-bc7e-dec230910658086b9f',
    '_ga_YXBDEHVL2V': 'GS1.1.1712028662.4.1.1712028667.0.0.0',
    '_ga': 'GA1.2.1542168158.1711483733'
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
    Error_message = "Error in the urls text file :" + str(error)
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

for i,url_url_id in enumerate(url_list):
    try:
        url,url_id=url_url_id.split(',')
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
        Ref_value = "35"
        print(url_id)

        soup = use_drive(url,request_cookies).find('div', class_='article-issue-info')
        Volume = re.sub(r'[^0-9]+', "", soup.find('div', class_='volume').text.strip())
        Issue = re.sub(r'[^0-9]+', "", soup.find('div', class_='issue').text.strip())
        Month,Year = soup.find('div', class_='ii-pub-date').text.strip().split(' ')
        All_articles = use_drive("https://journals.biologists.com" + soup.find('div', class_='view-current-issue').find('a').get('href'),request_cookies).find('div',class_='section-container').findAll('div', class_='al-article-item-wrap al-normal')
        i, j = 0, 0
        while i < len(All_articles):
            Article_link,Article_title=None,None
            try:
                Article_title = All_articles[i].find('h5', class_='item-title').find('a').text.strip()
                Article_link = "https://journals.biologists.com" + All_articles[i].find('h5', class_='item-title').find('a').get('href')
                if not Article_link in read_content:
                    Article_details=use_drive(Article_link,request_cookies)
                    pdf_link_check=Article_details.find('ul',class_='debug js-toolbar toolbar')
                    if pdf_link_check.find('li', class_='item-pdf'):
                        DOI = \
                        Article_details.find('div', class_='ww-citation-wrap-doi').find('a').text.strip().rsplit('doi.org/', 1)[-1].rstrip('.')
                        pdf_link='https://journals.biologists.com'+pdf_link_check.find('li', class_='item-pdf').find('a').get('href')
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
                                {"Title": Article_title, "DOI": DOI, "Publisher Item Type": "", "ItemID": "", "Identifier": "",
                                 "Volume": Volume, "Issue": Issue, "Supplement": "", "Part": "",
                                 "Special Issue": "", "Page Range": "", "Month": Month, "Day": "", "Year": Year,
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
                if j < 3:
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
    except Exception as error:
        Error_message = "Error in the driver :" + str(error)
        print(Error_message)
        error_list.append(Error_message)
        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list, len(completed_list),
                                             ini_path, attachment, current_date, current_time, Ref_value)

driver.quit()





