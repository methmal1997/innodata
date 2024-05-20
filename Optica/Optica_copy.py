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

            label_tag = soup2.find('label', class_='osap-accordion__label')
            if label_tag:
                # Extract the text from the label tag
                volume_text = label_tag.get_text(strip=True)

                # Find the index of the first space character
                space_index = volume_text.find(' ')

                # Extract the volume number
                if space_index != -1:
                    volume = volume_text[space_index + 1: volume_text.find(' ', space_index + 1)].strip()
                    # print(volume)
                else:
                    error_list = "Space not found after 'Vol.'"
                    error_list.append(Error_message)
                    print("Space not found after 'Vol.'")

            else:
                error_list = "Label tag not found."
                error_list.append(Error_message)
                print("Label tag not found.")

            ul_tag = soup2.find('ul', class_='volume-issue-list')
            first_li_tag = ul_tag.find('li')
            first_line_text = first_li_tag.get_text(strip=True)

            parts = first_line_text.split(',')
            issue = ''.join(filter(str.isdigit, parts[0].strip()))
            date = parts[1].strip()



        elif date_element:
            date_text = date_element.get_text(strip=True)
            parts = date_text.split(',')

            # Extracting date, volume, and issue
            date = parts[0].strip()  # "1 October 2023"
            volume = parts[1].strip().split()[1]  # "90"
            issue = parts[2].strip().split()[1]  # "10"

            print("Date:", date)
            print("Volume:", volume)
            print("Issue:", issue)
        else:
            Error_message = "Date not found in the HTML snippet."
            print(Error_message)
            error_list.append(Error_message)

        # print(current_soup)

    except:
        pass
