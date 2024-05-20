import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import common_function


def get_soup(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


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

def scrapper(url):
    payload = {'api_key': '7af826f113ca7a065f3e7b1f623431ee', 'url': url}
    r = requests.get('http://api.scraperapi.com', params=payload,)
    s = r.text
    # print(s)
    return s

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

    current_soup = get_soup(url)
    current_issue = current_soup.find('div', class_='view-current-issue')
    # print(current_issue)
    current_soup = scrapper(url)

    print(current_soup)

import re

# Input string
text = "https://doi.org/10.1242/dev.202889"

# Use regular expression to extract the DOI
doi = re.search(r'(?<=\bdoi.org\/)\d+\.\d+\/\w+.\d+', text).group(0)

# Print the extracted DOI
print(doi)

# Print the extracted DOI
print(doi)


