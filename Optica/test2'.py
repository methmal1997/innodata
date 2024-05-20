import requests
import undetected_chromedriver as uc
import time

url = "https://opg.optica.org/directpdfaccess/ead43835-9751-4942-bac7a266a0d9fd9c_548779/opn-35-4-10.pdf?da=1&id=548779&seq=0&mobile=no"

options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--user-agent=YOUR_USER_AGENT_STRING')
options.add_argument('--version_main=108')
driver = uc.Chrome(options=options)

def get_pdf_downloding_link(url):

    driver.get(url)
    time.sleep(5)
    current_url = driver.current_url
    return current_url


k = get_pdf_downloding_link(url)
print(k)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
pdf_content = requests.get(k, headers=headers).content
with open("output_fimeName.pdf", 'wb') as file:
    file.write(pdf_content)