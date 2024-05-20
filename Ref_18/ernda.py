import re
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import common_function
import pandas as pd

def get_soup(url):
    response = requests.get(url,headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

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
        url, url_id = url_url_id.split(',')
        current_datetime = datetime.now()
        current_date = str(current_datetime.date())
        current_time = current_datetime.strftime("%H:%M:%S")

        ini_path= os.path.join(os.getcwd(),"Info.ini")
        Download_Path,Email_Sent,Check_duplicate,user_id=common_function.read_ini_file(ini_path)
        print(url_id)
        duplicate_list = []
        error_list = []
        completed_list=[]
        data = []
        pdf_count = 1
        Ref_value="81"
        url_value=url.split('/')[-2]

        current_out=common_function.return_current_outfolder(Download_Path,user_id,url_id)
        out_excel_file=common_function.output_excel_name(current_out)

        current_soup=get_soup(url)
        Year_Month=current_soup.find('div',class_='papers-filter-selected').text.strip().split()
        Year=Year_Month[-1]
        Month=Year_Month[-2]
        Issue=re.sub(r'[^0-9]+','',Year_Month[3])
        Volume=re.sub(r'[^0-9]+','',Year_Month[1])


        All_articles=current_soup.find('div',class_='view-content').findAll('div',class_='views-row')
        for sin_art in All_articles:
            Article_link,Article_title=None,None
            try:
                Article_link ='https://www.iieta.org'+sin_art.find('div',class_='paper-title').find('a').get('href')
                Article_title = sin_art.find('div',class_='paper-title').find('a').text.strip()
                if not Article_link in read_content:
                    DOI=sin_art.find('div',class_='paper-doi').text.strip().rsplit('org/',1)[-1]
                    Page_range=sin_art.find('div',class_='paper-page').text.strip().rsplit('Page ',1)[-1]
                    pdf_link='https://www.iieta.org'+sin_art.find('div',class_='paper-download').find('a').get('href')
                    check_value = common_function.check_duplicate(DOI, Article_title, url_id, Volume, Issue)
                    if Check_duplicate.lower()=="true" and check_value:
                        message = f"{Article_link} - duplicate record with TPAID {{tpaid returned in response}}"
                        duplicate_list.append(message)
                        print("Duplicate Article :", Article_title)

                    else:
                        scrape_message = f"{Article_link}"
                        completed_list.append(scrape_message)
                        print("Original Article :", Article_title)
                        pdf_content = requests.get(pdf_link, headers=headers).content
                        output_fimeName = os.path.join(current_out,f"{pdf_count}.pdf")
                        with open(output_fimeName, 'wb') as file:
                            file.write(pdf_content)
                        data.append(
                            {"Title": Article_title, "DOI": DOI, "Publisher Item Type": "", "ItemID": "",
                             "Identifier": "",
                             "Volume": Volume, "Issue": Issue, "Supplement": "", "Part": "",
                             "Special Issue": "", "Page Range": Page_range, "Month": Month, "Day": "",
                             "Year": Year,
                             "URL": Article_link, "SOURCE File Name": f"{pdf_count}.pdf", "user_id": user_id})
                        df = pd.DataFrame(data)
                        df.to_excel(out_excel_file, index=False)
                        pdf_count += 1
                        completed_list.append(Article_link)
                        with open('completed.txt', 'a', encoding='utf-8') as write_file:
                            write_file.write(Article_link + '\n')
                else:
                    print("Already downloaded article :", Article_title)

            except Exception as error:
                message=f"Error link - {Article_link} : {str(error)}"
                print(f"{Article_title} : {str(error)}")
                error_list.append(message)
                All_articles.append(sin_art)

        if str(Email_Sent).lower() == "true":
            attachment_path = out_excel_file
            if os.path.isfile(attachment_path):
                attachment = attachment_path
            else:
                attachment = None
            common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,len(completed_list), ini_path, attachment, current_date, current_time,Ref_value)
        sts_file_path=os.path.join(current_out,'Completed.sts')
        with open(sts_file_path,'w') as sts_file:
            pass
    except Exception as error:
        Error_message = "Error in the site :" + str(error)
        print(Error_message)
        error_list.append(Error_message)
        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list, len(completed_list),
                                             ini_path, attachment, current_date, current_time, Ref_value)





