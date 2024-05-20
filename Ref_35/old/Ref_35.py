import time

import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import common_function
import pandas as pd
import random



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
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup



# try:
with open('urlDetails.txt', 'r', encoding='utf-8') as file:
    url_list = file.read().split('\n')

try:
    with open('completed.txt', 'r', encoding='utf-8') as read_file:
        read_content = read_file.read().split('\n')
except FileNotFoundError:
    with open('completed.txt', 'w', encoding='utf-8'):
        with open('completed.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().split('\n')

for i, url_url_id in enumerate(url_list):
    # try:
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
    Ref_value = "49"
    url_value = url.split('/')[-2]

    current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
    out_excel_file = common_function.output_excel_name(current_out)
    try:
        current_soup = get_soup(url)
        current_issue = current_soup.find('div', class_='view-current-issue')
        current_issue_link = current_soup.find('div', class_='view-current-issue').find('a').get('href')

    except:
        try:
            time.sleep(1)
            response = requests.get(url, proxies=get_random_proxy(), headers=headers)
            current_soup = BeautifulSoup(response.content, 'html.parser')
            current_issue = current_soup.find('div', class_='view-current-issue')
            current_issue_link = current_soup.find('div', class_='view-current-issue').find('a').get('href')
        except:
            captcha_main.captcha_main(url)


    current_issue_link = 'https://journals.biologists.com/'+current_issue_link

    response = requests.get(current_issue_link, proxies=get_random_proxy(), headers=headers)

    if response.status_code == 200:
        current_soup_2 = BeautifulSoup(response.content, 'html.parser')
        volume_issue = current_soup_2.find('span', class_='volume issue')

        volume_issue = current_soup_2.find('span', class_='volume issue').text.split(', ')
        volume = volume_issue[0].split()[1]
        issue = volume_issue[1].split()[1]
        date = current_soup_2.find('div', class_='ii-pub-date').text.split()
        month = date[0]
        year = date[1]


        articles_count = len(current_soup_2.find_all('div', class_='al-article-items'))
        articles_count_with_pdf = len(current_soup_2.find_all('a', class_='al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event  article-pdfLink'))
        status = 0
        print("Number of articles : ", articles_count)
        print("Number of articles with PDF : ", articles_count_with_pdf)

        article_sections = current_soup_2.find_all('div', class_='al-article-items')
        for section in article_sections:
            Article_title = section.find('h5',class_="customLink item-title").text
            # reasearch_link = section.find('a',class_="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event  article-pdfLink")
            # print(reasearch_link)
            if not Article_title in read_content:

                Article_link = 'https://journals.biologists.com'+section.find('h5',class_="customLink item-title").find('a').get('href')
                Pdf_link = section.find('a', class_="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event  article-pdfLink")
                print(Pdf_link)
                response = requests.get(Article_link, proxies=get_random_proxy(), headers=headers)

                if response.status_code == 200:
                    current_soup_pdf = BeautifulSoup(response.content, 'html.parser')
                    try:
                        DOI = current_soup_pdf.find('div', class_='citation-doi').text
                    except:
                        DOI = ''

                    check_value = common_function.check_duplicate(DOI, Article_title, url_id, volume,
                                                                  issue)

                    if Check_duplicate.lower() == "true" and check_value:
                        message = f"{Article_link} - duplicate record with TPAID {{tpaid returned in response}}"
                        duplicate_list.append(message)
                        print("Duplicate Article :", Article_title)

                    else:
                        scrape_message = f"{Article_link}"
                        completed_list.append(scrape_message)
                        print(Article_link)
                        pdf_content = requests.get(Article_link, headers=headers).content
                        output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                        with open(output_fimeName, 'wb') as file:
                            file.write(pdf_content)

                        data.append(
                            {"Title": Article_title, "DOI": DOI, "Publisher Item Type": "", "ItemID": "",
                             "Identifier": "",
                             "Volume": volume, "Issue": issue, "Supplement": "", "Part": "",
                             "Special Issue": "", "Page Range": "", "Month": month, "Day": "",
                             "Year": year,
                             "URL": Article_link, "SOURCE File Name": f"{pdf_count}.pdf",
                             "user_id": user_id})
                        df = pd.DataFrame(data)
                        df.to_excel(out_excel_file, index=False)
                        pdf_count += 1
                        completed_list.append(Article_link)

                        with open('completed.txt', 'a', encoding='utf-8') as write_file:
                            write_file.write(Article_link + '\n')
                        status += 1
                        print(
                            f"The total number of {articles_count} downloads {status} PDFs have downloded.")
                # except:
                # message = f"Error link - {Article_link} : {str(error)}"
                # print(f"{Article_title} : {str(error)}")
                # error_list.append(message)
                # All_articles.append(div)





                else:
                    Error_message = "Failed to navigate to the link. Status code:" + str(response.status_code)
                    print(Error_message)
                    error_list.append(Error_message)
                    common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                         len(completed_list),
                                                         ini_path, attachment, current_date, current_time, Ref_value)





    else:
        Error_message = "Failed to navigate to the link. Status code:" + str(response.status_code)
        print(Error_message)
        error_list.append(Error_message)
        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                             len(completed_list),
                                             ini_path, attachment, current_date, current_time, Ref_value)





        # except Exception as error:
        #
        #     Error_message = "Error in the site :" + str(error)
        #     print()
        #     print(Error_message)
        #     error_list.append(Error_message)
        #     common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
        #                                          len(completed_list),
        #                                          ini_path, attachment, current_date, current_time, Ref_value)




# except Exception as error:
#     Error_message = "Error in the urls text file :" + str(error)
#     print(Error_message)
#     error_list.append(Error_message)
#     common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list, len(completed_list),
#                                          ini_path, attachment, current_date, current_time, Ref_value)
