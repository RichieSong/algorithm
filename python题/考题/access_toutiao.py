# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  19/10/10 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.
"""
import requests,time

url  = "https://www.toutiao.com/i6746182662358040845/"
for i in range(2000):
    content = requests.get(url)
    if content.status_code == 200:
        print(content.text)
        time.sleep(1)
        print(i+1)