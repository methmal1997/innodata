import os
import urllib.parse
import pandas as pd
import requests
from bs4 import BeautifulSoup

given_source_id = 76648099
output_folder = "Output"



def execution():
    for index, row in df_doi_file.iterrows():
        if row["Source ID"] == given_source_id:
            doi_suffix = row['DOI']
            base_url = "https://www.thieme-connect.de/products/all/search"
            query_param = f"?query={doi_suffix}&radius=fulltext&option=AND&clearSavedProfileSearch=true"
            customized_url = base_url + query_param

            response = requests.get(customized_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                div_element = soup.find('div', id='list-searchresult')

                if div_element:
                    tab_content = div_element.find_all('div', class_='tabContentContainer')

                    if tab_content:
                        for div in tab_content:
                            if "Unfortunately there are no matches for your search. Please check your search request and try again." in div.text:
                                break
                        else:
                            tab_content_1 = div_element.find_all('div', class_='relatedArticles')
                            for div in tab_content_1:
                                anchor = div.find('a', class_='gotoLink')
                                if anchor:
                                    href = anchor.get('href')
                                    full_url = urllib.parse.urljoin('https://www.thieme-connect.de', href)

                                    response = requests.get(full_url)
                                    if response.status_code == 200:
                                        folder_name = os.path.join(output_folder, str(row["Order ID"]))
                                        if not os.path.exists(folder_name):
                                            os.makedirs(folder_name)
                                        file_name = os.path.basename(full_url)
                                        file_path = os.path.join(folder_name, file_name)
                                        with open(file_path, 'wb') as f:
                                            f.write(response.content)
                                        print(f"File '{file_name}' downloaded successfully.")
                                        df_doi_file.at[index, 'Download SI'] = 'Yes'
                                    else:
                                        print(f"Failed to download file from URL: {full_url}")

                    else:
                        print("Tab content divs not found within the div with ID 'content'.")
                else:
                    print("Div element with ID 'content' not found.")

            df_doi_file.to_csv("DOI List.csv", index=False)

    input("Download finished. Press Enter to exit...")


try:
    df_doi_file = pd.read_csv("./DOI List.csv")
    print(f"Successfully read the doi file : {df_doi_file}")

    try:
        with open('output.txt', 'r') as file:
            # Read the entire contents of the file
            content = file.read()
            output_folder = content + "/" + output_folder
            execution()
    except:
        print("output.txt which has absolute path not found")

except:
    print("DOI List.csv not found")








