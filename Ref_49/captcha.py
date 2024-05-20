# https://github.com/2captcha/2captcha-python

import sys
import os

import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

from twocaptcha import TwoCaptcha

api_key = 'a03589ed562de14589af1d772c2b41bb'

solver = TwoCaptcha(api_key)
# solver.solve_captcha()
result = solver.solve_captcha(
        site_key='6LfoPLQZAAAAAJeiXrDx2rycUOCbQ3fWpdNQnvPv',
        page_url='https://journals.biologists.com/crawlprevention/governor?content=%2fjournals')

'text/html; charset=utf-8'

def post_page(url, result):
    payload = {'userCaptchaResponse': result}  # Correct payload format
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    response = requests.post(url, data=payload, headers=headers)  # Use 'data' instead of 'payload'

    print(response.content)


post_page('https://journals.biologists.com/crawlprevention/governor?content=%2fjournals',result)

