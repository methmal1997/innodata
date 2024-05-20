import random
import time
import requests
import undeted

error_list = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

driver = undeted.main()
if not driver:
    Error_message = "Error in chrome driver or undeteted chrome :"
    print(Error_message)
    error_list.append(Error_message)


def get_current_cookies(url):
    driver = undeted.main()
    if not driver:
        Error_message = "Error in chrome driver or undeteted chrome :"
        print(Error_message)
        error_list.append(Error_message)
        return None
    driver.delete_all_cookies()
    driver.get(url)
    time.sleep(random.uniform(0, 3))
    selenium_cookies = driver.get_cookies()
    cookies_for_requests = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
    return cookies_for_requests

url = "https://www.pnas.org/toc/pnas/current"

response = requests.get(url, headers=headers,cookies=get_current_cookies(url))
print(response.content)
# print(get_current_cookies(url))
# print(get_current_cookies(url))
