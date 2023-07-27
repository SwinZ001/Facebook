# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:06:37 2021

@author: Akai
"""

import requests
import re
import os

if __name__ == "__main__":
    if not os.path.exists(r'G:\img\..'):
        os.mkdir(r'G:\img\..')
    i=1
    for page in range(140):
        url = "http://www.jj20.com/bz/nxxz/list_7_"+str(i)+".html"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'

        }
        response = requests.get(url=url, headers=headers)
        ata_obj = response.text
        ex = '<li>.*?<img src="(.*?)" width=.*?</li>'
        imgsrc_list = re.findall(ex, ata_obj, re.S)
        for src in imgsrc_list:
            image_data = requests.get(url=src, headers=headers).content
            img_name = src.split('/')[-1]
            img_path = r'G:\img\..' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(image_data)
                print("成功")