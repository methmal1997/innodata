import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver

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

chromedriver.install()  # This ensures the correct version of chromedriver is installed
driver = uc.Chrome(options=options)

print("Using undetected_chromedriver.")