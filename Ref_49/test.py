import requests
import webbrowser

id = "27a58878-5b38-49c4-a609-e0eef48295b0"

url = f'https://www.lcgdbzz.org/article/exportPdf?id={id}&language=en'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

# Send a GET request to download the PDF file directly
r = requests.get(url,headers=headers)

# Check if the request was successful
if r.status_code == 200:
    filename = f'output-{id}.pdf'

    # Write the content of the response to a PDF file
    with open(filename, 'wb') as fh:
        fh.write(r.content)
else:
    print("Failed to download the PDF. Status code:", r.status_code)
