import io
import json

import openpyxl as openpyxl
import requests
import re
from lxml import etree

if __name__ == "__main__":
    wb = openpyxl.Workbook()
    data_sheet = wb.active
    x=1
    y=2
    for page in range(1,13):
        url = 'https://dy.feigua.cn/AwemePromotion/PromotionSearch?duration=&hours=72&likes=1&sales=&pvyesterday=&cate0=115&sort=1&page='+str(page)+'&_=1629726436009'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
            'Cookie': 'ASP.NET_SessionId=ck02tolhrvhtftsc4geoigrh; Hm_lvt_876e559e9b273a58993289470c10403b=1629293572,1629646587; FEIGUA=UserId=7f5141150b143a34&NickName=feafe2faf038e7bb8d7e7e61837e68398c353fecd03b3017&checksum=0e640c9c1bc2&FEIGUALIMITID=ab54c1b6b1714ac8b330e8db47bd5dcb; 2eacea0f5a8404522a17a3646406f776=11c014ebad67002f7ad1f454a99db94f41771699532e2f059f162ef7fcc4279fd7d4118cb849b2032b2d8eea6c423c88d76e67004915c54b05546087a4587a4e50c3fee243ed5d832e5a45c346cfe3580efd366e9c29ad5514d2bb2238deedbeff22995d1d0a29eebab0cc8f3a619c55; SaveUserName=; Hm_lpvt_876e559e9b273a58993289470c10403b=1629646665'
        }
        response = requests.get(url=url, headers=headers)
        ata_obj = response.text
        tree = etree.HTML(ata_obj)
        kol_name=tree.xpath('//*[@class="item-title"]/a/text()')
        # kol_name_C=json.dumps(kol_name,encoding='utf-8',ensure_ascii=False)
        # print kol_name_C
        kol_id = tree.xpath('//*[@class="item-title"]/a/@data-awemeid')
        for i in range(0,len(kol_id)):
            data_list = []
            video_link='https://www.douyin.com/video/'+str(kol_id[i])+'?previous_page=app_code_link'
            # print kol_name[i]
            data_list.append(video_link)
            data_list.append(kol_name[i*2])
            data_sheet.append(data_list)
    wb.save('G:\cart_data.xls')
    print "over+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++over"


