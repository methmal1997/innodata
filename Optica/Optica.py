import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common_function

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
    error_list.append(Error_message)
    common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list, len(completed_list),
                                         ini_path, attachment, current_date, current_time, Ref_value)

for i, url_url_id in enumerate(url_list):
    try:
        url, url_id = url_url_id.split(',')
        current_datetime = datetime.now()
        current_date = str(current_datetime.date())
        current_time = current_datetime.strftime("%H:%M:%S")

        ini_path = os.path.join(os.getcwd(), "Ref_8.ini")
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
                        date_text = date_element_2.get_text(strip=True)
                        parts = date_text.split(',')

                        date = parts[0].strip()
                        volume = parts[1].strip().split()[1]
                        issue = parts[2].strip().split()[1]

                        article_title = soup3.find('p', class_='article-title')
                        page_numbers = soup3.find('p', style='color: #666').strong.next_sibling.strip()
                        page_numbers = page_numbers.split(',')[1].split('(')[0].strip()

                        pdf_link = soup3.find('a', id='link-pdf').get('href')
                        # uri = pdf_link.split('=')[1].split('&')[0]
                        # seq = pdf_link.split('=')[2]
                        #
                        # pdf_link = f"https://opg.optica.org/directpdfaccess/2b2990e8-dd24-4ec2-aa3346d2cd263ba9_548779/{uri}.pdf?da=1&id=548779&seq={seq}&mobile=no"

                        print(article_title)




                    else:
                        Error_message = "Date not found in the HTML snippet."
                        print(Error_message)
                        error_list.append(Error_message)



            else:
                print("No 'a' tag found within the first list item.")


        elif date_element:
            # Default page

            date_text = date_element.get_text(strip=True)
            parts = date_text.split(',')

            date = parts[0].strip()
            volume = parts[1].strip().split()[1]
            issue = parts[2].strip().split()[1]

            article_title = current_soup.find('p', class_='article-title').text
            page_numbers = current_soup.find('p', style='color: #666').strong.next_sibling.strip()
            page_numbers = page_numbers.split(',')[1].split('(')[0].strip()


        else:
            Error_message = "Date not found in the HTML snippet."
            print(Error_message)
            error_list.append(Error_message)

        # print(date)
        # print(volume)
        # print(issue)
        # print(article_title)
        # print(page_numbers)


    except Exception as error:

        Error_message = "Error in the site :" + str(error)
        print(Error_message)
        error_list.append(Error_message)
        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list, len(completed_list),
                                             ini_path, attachment, current_date, current_time, Ref_value)
