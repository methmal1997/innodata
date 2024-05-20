# print("hi")
# import captcha_main as captcha_main
#
#
# url = "https://journals.aai.org/immunohorizons"
# response = captcha_main.captcha_main(url)
#
# print(response)
import random
import time

import requests

import captcha_main

url = "https://journals.aai.org//immunohorizons/article-pdf/8/4/295/1655613/ih2300117.pdf"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers, allow_redirects=True)

final_url = response.url  # This will give you the final URL after redirection

print("Final URL after redirection:", final_url)

# print(response.content)


print("#########")


status = True
while status:
    time.sleep(random.uniform(5, 10))
    response = requests.get(url, headers=headers, allow_redirects=True)
    if response.status_code == 200:
        break
current_url = response.url

# response = captcha_main.captcha_main(url)
print(response.content)