import random
import time

from twocaptcha import TwoCaptcha
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}


def read_key_from_file(file_path):
    with open(file_path, 'r') as file:
        key = file.read().strip()
    return key

api_key = read_key_from_file('captcha_api.txt')
solver = TwoCaptcha(api_key)

def web_slover(url):

    result = solver.solve_captcha(
        site_key='6LfoPLQZAAAAAJeiXrDx2rycUOCbQ3fWpdNQnvPv',
        page_url=url)
    time.sleep(random.uniform(1, 3))
    return result

def post_page(url):

    result = web_slover(url)
    payload = {'userCaptchaResponse': result}
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #     # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    #     'Accept-Language': 'en-US,en;q=0.9,da;q=0.8',
    #     # 'Cache-Control': 'no-cache',
    #     'Connection': 'keep-alive',
    #     'Host': 'journals.biologists.com',
    #     # 'Pragma': 'no-cache',
    #     'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    #     'Sec-Ch-Ua-Mobile': '?0',
    #     'Sec-Ch-Ua-Platform': '"Windows"',
    #     'Sec-Fetch-Dest': 'document',
    #     'Sec-Fetch-Mode': 'navigate',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'Sec-Fetch-User': '?1',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    # }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'
    }

    response = requests.post(url, data=payload, headers=headers,timeout=40)

    return response