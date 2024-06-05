print("This is Ref_136")

import re
import time

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
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
attachment = None
url_id = None
current_date = None
current_time = None
Ref_value = None
ini_path = None

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
            Ref_value = "136"
            url_value = url.split('/')[-2]
            current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
            out_excel_file = common_function.output_excel_name(current_out)
            response = requests.get(url, headers=headers, timeout=50, verify=False)
            current_soup = BeautifulSoup(response.content, 'html.parser')
            target_div = current_soup.find('div', class_="yw_text_small persian").findAll('a', href=True)[-1]
            latest_issue_url = "https://fsct.modares.ac.ir/" + target_div['href']

            response_2 = requests.get(latest_issue_url, headers=headers, timeout=50, verify=False)
            current_soup_2 = BeautifulSoup(response_2.content, 'html.parser')
            vol_issue = current_soup_2.find('div', class_="yw_text persian").text.strip()
            match = re.search(r"Volume (\d+), Issue (\d+) \((\d{4})\)", vol_issue)
            volume = match.group(1)
            issue = match.group(2)
            year = match.group(3)

            articles = current_soup_2.find_all('div', class_='yw_text')
            filtered_articles = [article for article in articles if
                                 article.find('span', style='vertical-align:middle; direction:ltr')]

            filtered_articles = list(set(filtered_articles))
            c=1
            for article in filtered_articles:
                print(article)
                print("##############")
                print(c)
                print("##############")
                c = c + 1




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