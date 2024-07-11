import requests
from bs4 import BeautifulSoup
import time
import json


def mag_request(url, target):
    print(f"URL: {url}, Target: {target}")


def lsdy1(attach_type, article_id, qi_kan_wang_zhi, nian, issn):
    href = "https://example.com/CN/article/showArticleFile.do"  # Replace with window.location.href equivalent
    current_qk = qi_kan_wang_zhi
    if "/CN/" in href:
        current_qk = href.split("/CN/")[0]
    elif "/article/" in href:
        current_qk = href.split("/article/")[0]

    pars = {'attachType': attach_type, 'id': article_id, 'json': 'true'}
    response = requests.post(f"{current_qk}/CN/article/showArticleFile.do?{int(time.time() * 1000)}", data=pars)
    data = response.text

    if data.startswith('[json]'):
        json_data = json.loads(data.replace('[json]', ''))

        if json_data and json_data.get('status') == 1:
            if attach_type == "RICH_HTML":
                pars['token'] = json_data.get('clickRichToken')
                pars['referer'] = 'document.referrer'
                response = requests.post(
                    f"{qi_kan_wang_zhi}/CN/article/downloadArticleFileFee.do?{int(time.time() * 1000)}", data=pars)
                mag_request(json_data.get('richUrl'), "_blank")
            elif attach_type == "PDF_Mobile":
                mag_request(json_data.get('pdfMobileUrl'), json_data.get('downloadPdfTarget'))
            elif attach_type == "PDF_CN":
                mag_request(json_data.get('pdfCnUrl'), json_data.get('downloadPdfTarget'))
            else:
                mag_request(json_data.get('pdfUrl'), json_data.get('downloadPdfTarget'))
        elif json_data and json_data.get('status') == 4:
            gou_mai_article_checked(article_id, qi_kan_wang_zhi, json_data)
        else:
            print(f"Error: {data}")


def gou_mai_article_checked(article_id, qi_kan_wang_zhi, json_data):
    print("Purchase article logic here")


# Example usage
lsdy1('RICH_HTML', '8168', 'https://www.chinagp.net', '2024',
      'article/2024/1007-9572/8168/1007-9572-27-24-001.mag.shtml')
