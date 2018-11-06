#! /usr/bin/env python3


import requests
import os
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# 同じ階層にダウンロードフォルダ作成
foldername = 'downloaded'
os.makedirs(foldername, exist_ok=True)

print(os.getcwd())

# get page html
url = 'http://www2.toyo.ac.jp/~kawano/lec-semi/mat/'
res = requests.get(url)
res.raise_for_status()

# bs
soup = BeautifulSoup(res.text, 'lxml')
links = soup.find_all('a')

for link in links:
    relativepath = link.get('href')

    if os.path.basename(relativepath) != '':
        abspath = urljoin(url, relativepath)
        print('downloading...', abspath)

        # リンク先ファイルを保存
        data = requests.get(abspath)
        data.raise_for_status()

        filepath = os.path.join(foldername, relativepath)
        file = open(filepath, 'wb')
        for chunk in data.iter_content(100000):
            file.write(chunk)

        file.close()
        time.sleep(1)

print('download done.')
