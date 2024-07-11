print("This ref_8")

import warnings
warnings.filterwarnings("ignore")
import random
import os
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common_function
import time
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()
import pandas as pd
import captcha_main


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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}


def get_soup(url):
    response = requests.get(url, headers=headers,timeout=200)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


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


def get_pdf_downloding_link(url_1):
    driver.get(url_1)
    time.sleep(50)
    current_url = driver.current_url
    return current_url


try:
    try:
        with open('urlDetails.txt', 'r', encoding='utf-8') as file:
            url_list = file.read().split('\n')

            try:
                with open('completed.txt', 'r', encoding='utf-8') as read_file:
                    read_content = read_file.read().split('\n')
            except FileNotFoundError:
                with open('completed.txt', 'w', encoding='utf-8'):
                    with open('completed.txt', 'r', encoding='utf-8') as read_file:
                        read_content = read_file.read().split('\n')

    except Exception as error:
        Error_message = "Error in the urls text file :" + str(error)
        print(Error_message)
        input("Press Enter to exit...")
        error_list.append(Error_message)
        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list, len(completed_list),
                                             ini_path, attachment, current_date, current_time, Ref_value)

    for i, url_url_id in enumerate(url_list):
        try:

            url, url_id = url_url_id.split(',')
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
            Ref_value = "8"
            url_value = url.split('/')[-2]

            current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
            out_excel_file = common_function.output_excel_name(current_out)

            current_soup = get_soup(url)
            date_element = current_soup.find('h2', class_='heading-block-header').text.strip()

            date_pattern = r'\d{1,2} \w+ \d{4}'
            volume_issue_pattern = r'Volume (\d+), Issue (\d+)'

            date_match = re.search(date_pattern, date_element)
            date_str = date_match.group()
            date_obj = datetime.strptime(date_str, '%d %B %Y')
            Date = date_obj.strftime('%d')
            Year = date_obj.year
            Month = date_obj.strftime('%B')

            volume_issue_match = re.search(volume_issue_pattern, date_element)
            Volume = int(volume_issue_match.group(1))
            Issue = int(volume_issue_match.group(2))

            print(Date)
            print(Year)
            print(Month)
            print(Volume)
            print(Issue)
            Articles = current_soup.findAll("div", class_="media-twbs-body")
            articles_count_with_pdf = len(Articles)
            print(articles_count_with_pdf)
            status_pdf = 0
            for article in Articles:
                # try:
                Article_title = article.find("p",class_="article-title").text.strip()
                Article_link = "https://opg.optica.org"+article.find("p",class_="article-title").find("a")["href"]
                article_authors_tag = article.find('p', class_='article-authors')

                if article_authors_tag:
                    next_p_tag = article_authors_tag.find_next_sibling('p')
                    if next_p_tag:
                        page_range_text = next_p_tag.get_text().strip()
                        pattern = r'\b\d{1,4}-\d{1,4}\b'
                        Page_range = re.findall(pattern, page_range_text)[0]
                pdf_link = "https://opg.optica.org" + article.find("a",id="link-pdf")["href"]

                print(Article_title)
                print(Article_link)
                print(Page_range)
                print(pdf_link)

                check_value, tpa_id = common_function.check_duplicate(" ", Article_title, url_id, Volume,
                                                                      Issue)

                if Check_duplicate.lower() == "true" and check_value:
                    message = f"{Article_link} - duplicate record with TPAID : {tpa_id}"
                    duplicate_list.append(message)
                    print("Duplicate Article :", Article_title)

                else:
                    print("pdf_1.1 ")
                    status_1 = True
                    pdf_trail = 1

                    while status_1:
                        time.sleep(random.uniform(5, 10))
                        pdf_link = get_pdf_downloding_link(pdf_link)
                        response_pdf = requests.get(pdf_link, headers=headers, timeout=200,
                                                    allow_redirects=True)


                        if pdf_trail < 10 and response_pdf.status_code == 200:
                            print("pdf_1.2 - normal request succeed")
                            status_1 = False
                            break

                        elif pdf_trail == 10:

                            break
                        print("retrying pdf_1.1")
                        pdf_trail = pdf_trail + 1

                    while status_1:
                        time.sleep(random.uniform(5, 10))
                        pdf_link = get_pdf_downloding_link(pdf_link)
                        response_pdf = captcha_main.captcha_main(pdf_link)

                        if pdf_trail < 10 and response_pdf.status_code == 200:
                            print("pdf_2.2 - captcha request succeed")
                            status_1 = False
                            break

                        elif pdf_trail == 10:
                            Error_message = f"PDF viewing failed. it may resul empty filed downloding -: {Article_title}"
                            print(Error_message)
                            print("###########")
                            error_list.append(Error_message)
                            break
                        print("retrying captcha_2.1")
                        pdf_trail = pdf_trail + 1


                    if not status_1:

                        pdf_content = response_pdf.content
                        output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")

                        with open(output_fimeName, 'wb') as file:
                            file.write(pdf_content)

                        data.append(
                            {"Title": Article_title, "DOI": "", "Publisher Item Type": "", "ItemID": "",
                             "Identifier": "",
                             "Volume": Volume, "Issue": Issue, "Supplement": "", "Part": "",
                             "Special Issue": "", "Page Range": Page_range, "Month": Month, "Day": Date,
                             "Year": Year,
                             "URL": pdf_link, "SOURCE File Name": f"{pdf_count}.pdf", "user_id": user_id})

                        df = pd.DataFrame(data)
                        df.to_excel(out_excel_file, index=False)
                        pdf_count += 1
                        scrape_message = f"{Article_link}"
                        completed_list.append(scrape_message)
                        with open('completed.txt', 'a', encoding='utf-8') as write_file:
                            write_file.write(Article_title + '\n')
                        print(Article_title)
                        status_pdf += 1
                        print(f"The total number of PDFs {articles_count_with_pdf} , {status_pdf} PDF have been downloded...")
                        print("###########")

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
    Error_message = "Error in the main process :"

    error_list.append(str(Error_message))
    log_file_path = os.path.join('log.txt')
    with open(log_file_path, 'w') as log_file:
        log_file.write(str(Error_message) + '\n')

