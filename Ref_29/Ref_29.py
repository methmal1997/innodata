import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common_function
import pandas as pd

duplicate_list = []
error_list = []
completed_list = []
attachment = None
url_id = None
current_date = None
current_time = None
Ref_value = None
ini_path = None

try:
    with open('urlDetails.txt', 'r', encoding='utf-8') as file:
        url_list = file.read().split('\n')

    try:
        with open('completed.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().split('\n')
    except FileNotFoundError:
        with open('completed.txt', 'w', encoding='utf-8'):
            with open('completed.txt', 'r', encoding='utf-8') as read_file:
                read_content = read_file.read().split('\n')

    with requests.Session() as ss:

        for i, url_url_id in enumerate(url_list):
            try:
                url, url_id = url_url_id.split(',')
                current_datetime = datetime.now()
                current_date = str(current_datetime.date())
                current_time = current_datetime.strftime("%H:%M:%S")

                ini_path = os.path.join(os.getcwd(), "Ref_29.ini")
                Download_Path, Email_Sent, Duplicate_Check, User_id = common_function.read_ini_file(ini_path)
                current_out = common_function.return_current_outfolder(Download_Path, User_id, url_id)
                out_excel_file = common_function.output_excel_name(current_out)
                Ref_value = "29"

                print(url_id)
                duplicate_list = []
                error_list = []
                completed_list = []
                final_data_list = []
                pdf_count = 1

                main_page = ss.get(url)
                if main_page.status_code == 200:
                    main_soup = BeautifulSoup(main_page.content, "lxml")

                    # Extract meta data
                    vol_issue_nav = main_soup.find("div", {"class": "qknr"})
                    vol_issue = str(vol_issue_nav.find("span").text).replace('\r\n\t\t\t', " ")

                    vol_issue_split = vol_issue.split(' ')
                    volume = vol_issue_split[1]
                    issue = vol_issue_split[3]
                    day = vol_issue_split[4]
                    month = vol_issue_split[5]
                    year = vol_issue_split[6]

                    # get table content
                    table_content = main_soup.find_all("div", {"class": "noselectrow"})
                    for row in table_content:
                        try:

                            Id = str(row["id"]).replace("art", "")
                            tittle = row.find("a", {"class": "biaoti_en"}).text
                            if not tittle in read_content:

                                doi = ""
                                page_range_navi = (
                                    str(row.find("dd", {"class": "kmnjq"}).text).replace("\r", "").replace("\n",
                                                                                                           "").replace(
                                        "\t",
                                        "")).split(" ")
                                get_page_range = str(page_range_navi[len(page_range_navi) - 1]).split(':')
                                page_range = (get_page_range[len(get_page_range) - 1]).replace('.', '').strip()

                                pdf_link = 'http://gsytb.jtxb.cn/EN/article/downloadArticleFile.do?attachType=PDF&id=' + Id

                                # check if the article is duplicate or not
                                check_value = common_function.check_duplicate(doi, tittle, url_id, volume,
                                                                              issue)
                                if str(Duplicate_Check).lower() == "true" and check_value:
                                    message = (f"{pdf_link} - duplicate record with TPAID {{tpaid returned in "
                                               f"response}}")
                                    duplicate_list.append(message)
                                    print("Duplicate Article :", tittle)

                                else:
                                    print("Original Article :", tittle)

                                    pay_load = {
                                        "attachType": "PDF",
                                        "id": Id
                                    }

                                    pdf_download_headers = {
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'Accept-Encoding': 'gzip, deflate',
                                        'Accept-Language': 'en-US,en;q=0.9',
                                        'Connection': 'keep-alive',
                                        # 'Cookie': 'JSESSIONID=5560DE71E0F2CD2E3D88C7CC834476A1; wkxt3_csrf_token=cc8592e1-aa9c-4b09-b366-06686f675aa2',
                                        'Host': 'gsytb.jtxb.cn',
                                        'Referer': 'http://gsytb.jtxb.cn/EN/1001-1625/home.shtml',
                                        'Upgrade-Insecure-Requests': '1',
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
                                    }


                                    pdf_res = ss.get(pdf_link, headers=pdf_download_headers, data=pay_load)
                                    if pdf_res.status_code == 200:
                                        pdf_content = pdf_res.content
                                        output_fimeName = os.path.join(current_out, f"{pdf_count}.pdf")
                                        with open(output_fimeName, 'wb') as file:
                                            file.write(pdf_content)

                                        final_data_list.append(
                                            {"Title": tittle, "DOI": doi, "Publisher Item Type": "", "ItemID": "",
                                             "Identifier": "",
                                             "Volume": volume, "Issue": issue, "Supplement": "", "Part": "",
                                             "Special Issue": "", "Page Range": page_range, "Month": month,
                                             "Day": day,
                                             "Year": year,
                                             "URL": pdf_link, "SOURCE File Name": f"A{pdf_count}.pdf",
                                             "user_id": User_id})
                                        df = pd.DataFrame(final_data_list)
                                        df.to_excel(out_excel_file, index=False)

                                        completed_list.append(tittle)
                                        with open('completed.txt', 'a', encoding='utf-8') as write_file:
                                            write_file.write(tittle + '\n')

                                        pdf_count += 1
                            else:
                                print("Already downloaded article :", tittle)
                        except Exception as error:
                            message = f"Error title - {tittle} : {str(error)}"
                            print(f"{tittle} : {str(error)}")
                            error_list.append(str(message))
                            log_file_path = os.path.join(current_out, 'log.txt')
                            with open(log_file_path, 'w') as log_file:
                                log_file.write(str(message) + '\n')

                    if str(Email_Sent).lower() == "true":
                        attachment_path = out_excel_file
                        if os.path.isfile(attachment_path):
                            attachment = attachment_path
                        else:
                            attachment = None
                        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                             len(completed_list), ini_path, attachment,
                                                             current_date,
                                                             current_time, Ref_value)
                    sts_file_path = os.path.join(current_out, 'Completed.sts')
                    with open(sts_file_path, 'w') as sts_file:
                        pass
                else:
                    log_file_path = os.path.join(current_out, 'log.txt')
                    with open(log_file_path, 'w') as log_file:
                        log_file.write(str(main_page.status_code) + ' - Site not found' + '\n')
            except Exception as error:
                Error_message = "Error in the site :" + str(error)
                print(Error_message)
                error_list.append(Error_message)
                common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                     len(completed_list), ini_path, attachment, current_date,
                                                     current_time, Ref_value)
                log_file_path = os.path.join(current_out, 'log.txt')
                with open(log_file_path, 'w') as log_file:
                    log_file.write(str(Error_message) + '\n')

except Exception as error:
    print(error)
    Error_message = "Error in the main process :" + str(error)
    error_list.append(str(Error_message))
    log_file_path = os.path.join(current_out, 'log.txt')
    with open(log_file_path, 'w') as log_file:
        log_file.write(str(Error_message) + '\n')
