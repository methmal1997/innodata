import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common_function
import time
import undetected_chromedriver as uc
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
    response = requests.get(url, headers=headers)
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
    time.sleep(5)
    current_url = driver.current_url
    return current_url




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
        date_element = current_soup.find('h2', class_='heading-block-header')

        if 'All Issues' in date_element.text.split('\n'):

            html_content = current_soup.find('div', class_='osap-accordion').prettify()
            soup2 = BeautifulSoup(html_content, 'html.parser')
            first_list_item = soup2.find('li', class_='volume-issue-list__list-item')
            a_tag = first_list_item.find('a')

            if a_tag:

                href_link = "https://opg.optica.org/opn/" + a_tag['href']
                response = requests.get(href_link)
                if response.status_code == 200:
                    page_content = response.content
                    soup3 = BeautifulSoup(page_content, 'html.parser')

                    date_element_2 = soup3.find('h2', class_='heading-block-header')

                    if date_element_2:
                        parts = date_element_2.get_text(strip=True).split(',')
                        date = parts[0].strip()
                        volume = parts[1].strip().split()[1]
                        issue = parts[2].strip().split()[1]

                        All_articles = list(set(soup3.findAll('div', class_='media-twbs-body')))

                        for sin_art in All_articles:

                            Article_link, Article_title = None, None
                            Article_link_url = "https://opg.optica.org" + sin_art.find('a',id='link-pdf').get('href')

                            try:
                                Article_title = sin_art.find('p', class_='article-title').text
                                if not Article_link_url in read_content:

                                    page_numbers = sin_art.find('p', style='color: #666').strong.next_sibling.strip()
                                    page_numbers = page_numbers.split(',')[1].split('(')[0].strip()

                                    check_value = common_function.check_duplicate('', Article_title, url_id, volume,
                                                                                  issue)

                                    if Check_duplicate.lower() == "true" and check_value:
                                        message = f"{Article_link_url} - duplicate record with TPAID {{tpaid returned in response}}"
                                        duplicate_list.append(message)
                                        print("Duplicate Article :", Article_title)

                                    else:
                                        scrape_message = f"{Article_link_url}"
                                        completed_list.append(scrape_message)
                                        pdf_link = get_pdf_downloding_link(Article_link_url)
                                        response = requests.get(pdf_link, headers=headers)
                                        print(pdf_link)
                                        soup_test = str(BeautifulSoup(response.content, 'html.parser'))
                                        if soup_test=="Bad Request":
                                            response = captcha_main.captcha_main(pdf_link)
                                        pdf_content = response.content
                                        output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")

                                        with open(output_fimeName, 'wb') as file:
                                            file.write(pdf_content)
                                            data.append(
                                                {"Title": Article_title, "DOI": "", "Publisher Item Type": "",
                                                 "ItemID": "",
                                                 "Identifier": "",
                                                 "Volume": volume, "Issue": issue, "Supplement": "", "Part": "",
                                                 "Special Issue": "", "Page Range": page_numbers, "Month": date,
                                                 "Day": "",
                                                 "Year": date,
                                                 "URL": Article_link_url, "SOURCE File Name": f"{pdf_count}.pdf",
                                                 "user_id": user_id})
                                            df = pd.DataFrame(data)
                                            df.to_excel(out_excel_file, index=False)
                                            pdf_count += 1
                                            completed_list.append(Article_link_url)
                                            with open('completed.txt', 'a', encoding='utf-8') as write_file:
                                                write_file.write(Article_link_url + '\n')
                                else:
                                    print("Already downloaded article :", Article_title)

                            except Exception as error:
                                message = f"Error link - {Article_link_url} : {str(error)}"
                                print(f"{Article_title} : {str(error)}")
                                error_list.append(message)
                                All_articles.append(sin_art)

                    else:
                        Error_message = "Date not found in the HTML snippet."
                        print(Error_message)
                        error_list.append(Error_message)



        elif date_element:

            if date_element:
                parts = date_element.get_text(strip=True).split(',')
                date = parts[0].strip()
                volume = parts[1].strip().split()[1]
                issue = parts[2].strip().split()[1]

                All_articles = list(set(current_soup.findAll('div', class_='media-twbs-body')))

                for sin_art in All_articles:
                    Article_link, Article_title = None, None
                    Article_link_url = "https://opg.optica.org" + sin_art.find('a', id='link-pdf').get('href')

                    try:
                        Article_title = sin_art.find('p', class_='article-title').text
                        if not Article_link_url in read_content:

                            page_numbers = sin_art.find('p', style='color: #666').strong.next_sibling.strip()
                            page_numbers = page_numbers.split(',')[1].split('(')[0].strip()

                            check_value = common_function.check_duplicate('', Article_title, url_id, volume,
                                                                          issue)

                            if Check_duplicate.lower() == "true" and check_value:
                                message = f"{Article_link_url} - duplicate record with TPAID {{tpaid returned in response}}"
                                duplicate_list.append(message)
                                print("Duplicate Article :", Article_title)

                            else:
                                scrape_message = f"{Article_link_url}"
                                completed_list.append(scrape_message)
                                pdf_link = get_pdf_downloding_link(Article_link_url)
                                response = requests.get(pdf_link)
                                print(response)
                                pdf_content = requests.get(pdf_link, headers=headers).content
                                print(pdf_link)
                                output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")

                                with open(output_fimeName, 'wb') as file:
                                    file.write(pdf_content)
                                    data.append(
                                        {"Title": Article_title, "DOI": "", "Publisher Item Type": "", "ItemID": "",
                                         "Identifier": "",
                                         "Volume": volume, "Issue": issue, "Supplement": "", "Part": "",
                                         "Special Issue": "", "Page Range": page_numbers, "Month": date, "Day": "",
                                         "Year": date,
                                         "URL": Article_link_url, "SOURCE File Name": f"{pdf_count}.pdf",
                                         "user_id": user_id})
                                    df = pd.DataFrame(data)
                                    df.to_excel(out_excel_file, index=False)
                                    pdf_count += 1
                                    completed_list.append(Article_link_url)
                                    with open('completed.txt', 'a', encoding='utf-8') as write_file:
                                        write_file.write(Article_link_url + '\n')
                        else:
                            print("Already downloaded article :", Article_title)

                    except Exception as error:
                        message = f"Error link - {Article_link_url} : {str(error)}"
                        print(f"{Article_title} : {str(error)}")
                        error_list.append(message)
                        All_articles.append(sin_art)

            else:
                Error_message = "Date not found in the HTML snippet."
                print(Error_message)
                error_list.append(Error_message)



    except Exception as error:

        Error_message = "Error in the site :" + str(error)
        print(Error_message)
        input("Press Enter to exit...")
        error_list.append(Error_message)
        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list, len(completed_list),
                                             ini_path, attachment, current_date, current_time, Ref_value)

# input("Download finished. Press Enter to exit...")
