import time

import captcha_main
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import common_function
import pandas as pd
import random
import re

url = "https://journals.biologists.com/dev"
response = captcha_main.captcha_main(url)

print(response.content)