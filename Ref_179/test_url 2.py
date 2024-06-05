import requests
from bs4 import BeautifulSoup
import json


def get_current_issue():

    response=requests.post("http://www.cjco.cn/data/catalog/catalogMap")
    soup=json.loads(BeautifulSoup(response.content,'html.parser').text)
    year_key = str(list(soup["data"]["archive_list"].keys())[0])
    issue=soup["data"]["archive_list"][year_key][0]["issue"]
    link=f"http://www.cjco.cn/cn/article/{year_key}/{issue}"

    return link

print(get_current_issue())