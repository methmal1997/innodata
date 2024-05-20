import os
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

url = "https://opg.optica.org/captcha/(S(vhkl13yyct1hcelrjdwhgj0j))/?guid=DC3EFED9-5EEA-4069-AFB2-2C4FF91C9FD2"


response = requests.get(url, headers=headers)
soup = str(BeautifulSoup(response.content, 'html.parser'))

print(soup=="Bad Request")