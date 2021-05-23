import requests
import os
from bs4 import BeautifulSoup
from datetime import date
from urllib.parse import urlparse
from urllib.parse import unquote

acafeUrl = 'https://acafe.msc.sony.jp/index/choice'
currentDir = os.path.dirname(os.path.realpath('__file__'))
wallpaperFolder = '/download/'
downloadPath = currentDir + wallpaperFolder
if not os.path.exists(downloadPath):
    os.makedirs(downloadPath)

r = requests.get(acafeUrl)

if r.status_code == requests.codes.ok:
    data = r.json()
    soup = BeautifulSoup(data['result'], 'html.parser')

    # print(soup.prettify())

    items = soup.select('div[class="choice-bg"] img')
    for i in items:
        url = urlparse(unquote(unquote(i.get('src')))).query[4:].split("&",1)[0]
        filename = date.today().strftime("%Y%m%d_") + url.split("/")[-1]

        with open(downloadPath + filename, 'wb') as handle:
            imageRsp = requests.get(url, stream=True)
            if imageRsp.status_code == requests.codes.ok:
                for block in imageRsp.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)