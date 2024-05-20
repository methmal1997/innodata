from captcha_slover import post_page
import time
import undetected_chromedriver as uc
import random
import requests


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




def captcha_main(url):

    time.sleep(random.uniform(0, 3))
    status = True
    while status:
        time.sleep(random.uniform(5, 10))
        response = requests.get(url, headers=headers, allow_redirects=True)
        if response.status_code == 200:
            break
    current_url = response.url
    time.sleep(random.uniform(1, 4))
    response = post_page(current_url)

    return response

def current_url(url):
    status = True
    while status:
        time.sleep(random.uniform(5, 10))
        response = requests.get(url, headers=headers, allow_redirects=True)
        if response.status_code == 200:
            break
    current_url = response.url
    return current_url

