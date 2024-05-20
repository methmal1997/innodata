import os

import requests
import random
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

url = "https://www.pnas.org/doi/10.1073/pnas.2405386121"


response = requests.get(url,headers=headers)
current_soup_2 = BeautifulSoup(response.content,'html.parser')
path_parts = urlparse(current_soup_2.find('a',property="sameAs").text).path.split('/')
DOI = '/'.join(path_parts[1:])
Indentifier = current_soup_2.find('span',property="identifier").text

# https://www.pnas.org/doi/pdf/{DOI}?download=true
Pdf_link = f"https://www.pnas.org/doi/pdf/{DOI}"
response = requests.get(Pdf_link, headers=headers)
pdf_content = response.content
current_out = r"C:\Users\SL1184\PycharmProjects\Spec_project\Ref_18\download"

output_fimeName = os.path.join(current_out, f"1.pdf")

with open(output_fimeName, 'wb') as file:
    file.write(pdf_content)
# pdf_content = response.content

