print("This is Ref_122")

import re
import time

import requests
from bs4 import BeautifulSoup
import os
import sys
from datetime import datetime
import common_function
import pandas as pd
from PyPDF2 import PdfReader


print("This is Ref_122")
def read_pdf(pdf_path):
    file_path = pdf_path
    reader = PdfReader(file_path)
    text=re.sub(r'\s+'," ",reader.pages[0].extract_text()).rsplit('期 ',1)[-1].split(".")[0]
    Month=datetime.strptime(text, '%b').strftime('%B')
    return Month

def get_soup(url):
    response = requests.get(url,headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

def print_bordered_message(message):
    print()


def get_ordinal_suffix(n):
    if 11 <= n % 100 <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
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


print("Process started...")
print("This may take sometime.Please wait..........")
print("Urldetails text file was readed......")

try:
    with open('urlDetails.txt','r',encoding='utf-8') as file:
        url_list=file.read().split('\n')
except Exception as error:
    Error_message = "Error in the \"urlDetails\" : " + str(error)
    print(Error_message)
    error_list.append(Error_message)
    common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                         len(completed_list),
                                         ini_path, attachment, current_date, current_time, Ref_value)
    # common_function.email_body_html(current_date, current_time, duplicate_list, error_list, completed_list,
    #                                 len(completed_list), url_id, Ref_value, attachment, current_out)

try:
    with open('completed.txt', 'r', encoding='utf-8') as read_file:
        read_content = read_file.read().split('\n')
except FileNotFoundError:
    with open('completed.txt', 'w', encoding='utf-8'):
        with open('completed.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().split('\n')

url_index, url_check = 0, 0
while url_index < len(url_list):
    try:
        url, url_id = url_list[url_index].split(',')
        print(f"Executing this {url}")
        current_datetime = datetime.now()
        current_date = str(current_datetime.date())
        current_time = current_datetime.strftime("%H:%M:%S")

        if url_check == 0:

            ini_path = os.path.join(os.getcwd(), "Info.ini")
            Download_Path, Email_Sent, Check_duplicate, user_id = common_function.read_ini_file(ini_path)
            current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
            out_excel_file = common_function.output_excel_name(current_out)

        Ref_value = "122"

        duplicate_list = []
        error_list = []
        completed_list=[]
        data = []
        pdf_count = 1
        url_value=url.split('/')[-3]


        currentSoup=get_soup("https://www.hjgcjsxb.org.cn"+get_soup(url).find("li",{"type":"currentIssue_en"}).find("a").get("href"))

        try:
            volumeIssue=currentSoup.find("div",class_="article-list-title").text.strip().split()

            try:
                Year=re.sub(r'[^0-9]+','',volumeIssue[0])
            except:
                print("Failed to capture year")
                Year=""

            try:
                Volume=re.sub(r'[^0-9]+','',volumeIssue[1])
            except:
                print("Failed to capture volume")
                Volume=""

            try:
                Issue=re.sub(r'[^0-9]+','',volumeIssue[2])
            except:
                print("Failed to capture issue")
                Issue=""

        except:
            print("Failed to find year, volume and issue")
            Volume,Issue,Year="","",""

        All_articles = currentSoup.find("div",class_="articleListBox active base-catalog").findAll("div",class_="article-list",id=True)

        article_index, article_check = 0, 0
        while article_index < len(All_articles):
            Article_link, Article_title = None, None
            try:
                Article_title= re.sub(r'\s+'," ",All_articles[article_index].find("div",class_="article-list-title").find("a").text.strip())
                Article_link=All_articles[article_index].find("div",class_="article-list-title").find("a").get("href")
                id=All_articles[article_index].get("id")
                try:
                    doiPageRange=All_articles[article_index].find("div",class_="article-list-time")

                    try:
                        Page_range=doiPageRange.find('font').text.strip().split()[-1].rstrip('.')
                    except:
                        print("Failed to find page range")
                        Page_range=""

                    try:
                        DOI=doiPageRange.findAll('font')[1].find("a").text.strip()
                    except:
                        print("Failed to find DOI")
                        DOI=""

                except:
                    print("Failed to find doi and page range")
                    DOI,Page_range="",""

                pdf_link=f"https://www.hjgcjsxb.org.cn/article/exportPdf?id={id}&language=en"

                check_value, tpa_id = common_function.check_duplicate(DOI, Article_title, url_id, Volume, Issue)

                if Check_duplicate.lower() == "true" and check_value:
                    message = f"{Article_link} - duplicate record with TPAID : {tpa_id}"
                    duplicate_list.append(message)
                    print("Duplicate Article :", Article_title,"\n")

                else:

                    pdf_content = requests.get(pdf_link, headers=headers).content
                    output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                    with open(output_fimeName, 'wb') as file:
                        file.write(pdf_content)

                    try:
                        Month=read_pdf(output_fimeName)
                    except:
                        Month=""

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
                    scrape_message = f"{Article_link}"
                    completed_list.append(scrape_message)
                    print("Original Article :", Article_title,"\n")

                if not pdf_link in read_content:
                    with open('completed.txt', 'a', encoding='utf-8') as write_file:
                        write_file.write(pdf_link + '\n')

                article_index, article_check = article_index + 1, 0

            except Exception as error:
                if article_check < 4:
                    article_check += 1
                else:
                    message = f"{Article_link} : {str(error)}"
                    print("Download failed :", Article_title,"\n")
                    error_list.append(message)
                    article_index, article_check = article_index + 1, 0

        if str(Email_Sent).lower() == "true":
            attachment_path = out_excel_file
            if os.path.isfile(attachment_path):
                attachment = attachment_path
            else:
                attachment = None
            common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                 len(completed_list), ini_path, attachment, current_date,
                                                 current_time, Ref_value)
            # common_function.email_body_html(current_date, current_time, duplicate_list, error_list, completed_list,
            #                                 len(completed_list), url_id, Ref_value, attachment, current_out)
        sts_file_path = os.path.join(current_out, 'Completed.sts')
        with open(sts_file_path, 'w') as sts_file:
            pass

        url_index, url_check = url_index + 1, 0
    except Exception as error:
        if url_check < 4:
            url_check += 1
        else:
            Error_message = "Error in the site:" + str(error)
            print(Error_message,"\n")
            error_list.append(Error_message)
            common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                 len(completed_list),
                                                 ini_path, attachment, current_date, current_time, Ref_value)
            # common_function.email_body_html(current_date, current_time, duplicate_list, error_list, completed_list,
            #                                 len(completed_list), url_id, Ref_value, attachment, current_out)

            url_index, url_check = url_index + 1, 0