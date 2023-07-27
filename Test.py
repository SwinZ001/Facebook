import json
from time import sleep

import openpyxl
from lxml import etree

import requests
from selenium import webdriver
# from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.chrome.options import Options
# wb = openpyxl.Workbook()
# cart_data_sheet = wb.active

# url = 'https://dy.feigua.cn/api/v1/aweme/search/list?pageSize=10&pageIndex=1&sort=0&period=6&dateFrom=2022-03-19&dateTo=2022-03-19&_=1647620982538'
# headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
#             'Cookie': 'Hm_lvt_b9de64757508c82eff06065c30f71250=1636549762; chl=key=feigua2_baidu-pinzhuan; ASP.NET_SessionId=llv1wjqgtdeeb30nswihb3pn; Hm_lvt_876e559e9b273a58993289470c10403b=1647607059; FEIGUA=UserId=0c4d8af55e3529993cd7d3c1d97e1dda&NickName=9db1c403a424acb933dff3798a704f2bb5369475695da75061ccd07c99a58a18&checksum=84b441686f37&FEIGUALIMITID=ff29a677bd384172adf9b592064c08a7; 3b99f4eb12d4081e11c57420e45ab5f2=11c014ebad67002f9ba5bc3a4abd90b6526906ee58b41019b96baec54827a2ee31c054a9f8bbb7cc33db6f0444f1257e339ae1aedfa0ddfe18dcabf91d20934cfdc7d4641ecc4ce52585f5b303cbe0db0f5fcd503e43655758d6f3ad5a71eaf72eb5c2b1e6feced6e8e23e3c5a737a8a; SaveUserName=18998802954; Hm_lpvt_876e559e9b273a58993289470c10403b=1647620975'
#         }

# response = requests.get(url=url, headers=headers, verify=False)
# response.encoding="utf-8"
# 获取网页HTML代码
# ata_obj = response.text
# tree = etree.HTML(ata_obj)
# print(ata_obj)
# 获取网址返回的json数据
# sixTime_obj = response.json()
# print(sixTime_obj["Data"]["AwemeList"])
# for i in range(len(sixTime_obj["Data"]["AwemeList"])):
#     data_list = []
#     data_list.append(sixTime_obj["Data"]["AwemeList"][i]["BloggerNickName"])
#     data_list.append(sixTime_obj["Data"]["AwemeList"][i]["Desc"])
#     data_list.append(sixTime_obj["Data"]["AwemeList"][i]["VideoUrl"])
#     data_list.append(sixTime_obj["Data"]["AwemeList"][i]["CoverUrl"])
#     cart_data_sheet.append(data_list)
# wb.save('G:\cart_data.xls')
# print ("over+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++over")






# option=Options()
# 伪识别
# option.add_argument('--disable-blink-features=AutomationControlled')
# 无界面浏览器
# option.add_argument('--headless')
# bro = webdriver.Chrome(executable_path='F:\python\python3.9.10\Scripts\chromedriver.exe',chrome_options=option)
# bro.get("https://dy.feigua.cn/Member#/staticpage/video")
# # bro.get("https://www.51job.com/")
# # 获取cookies
# # sleep(30)
# # with open("cookies2.txt","w") as f:
# #     f.write(json.dumps(bro.get_cookies()))
# # bro.close()
# # bro.delete_all_cookies()
# # 用cookies登录
# with open("cookies2.txt","r") as f:
#     cookies_list=json.load(f)
#     for cookie in cookies_list:
#         bro.add_cookie(cookie)
# sleep(10)
# bro.refresh()
# bro.get("https://dy.feigua.cn/Member#/staticpage/video")





# option=Options()
# option.add_argument('--disable-blink-features=AutomationControlled')
# # option.add_argument('--headless')
# bro = webdriver.Chrome(executable_path='F:\python\python3.9.10\Scripts\chromedriver.exe',chrome_options=option)
# bro.get("https://www.51job.com/")
# sleep(2)
# # .//*[@target="_blank"],加点就是当前组件内的子组件，不加就是整个html文件的子组件
# aa=bro.find_element_by_xpath('/html/body/div[5]/div[2]/div').find_elements_by_xpath('.//*[@target="_blank"]')
# print(aa)



url = 'https://www.51job.com/'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
            'Cookie': 'Hm_lvt_b9de64757508c82eff06065c30f71250=1636549762; chl=key=feigua2_baidu-pinzhuan; ASP.NET_SessionId=llv1wjqgtdeeb30nswihb3pn; Hm_lvt_876e559e9b273a58993289470c10403b=1647607059; FEIGUA=UserId=0c4d8af55e3529993cd7d3c1d97e1dda&NickName=9db1c403a424acb933dff3798a704f2bb5369475695da75061ccd07c99a58a18&checksum=84b441686f37&FEIGUALIMITID=ff29a677bd384172adf9b592064c08a7; 3b99f4eb12d4081e11c57420e45ab5f2=11c014ebad67002f9ba5bc3a4abd90b6526906ee58b41019b96baec54827a2ee31c054a9f8bbb7cc33db6f0444f1257e339ae1aedfa0ddfe18dcabf91d20934cfdc7d4641ecc4ce52585f5b303cbe0db0f5fcd503e43655758d6f3ad5a71eaf72eb5c2b1e6feced6e8e23e3c5a737a8a; SaveUserName=18998802954; Hm_lpvt_876e559e9b273a58993289470c10403b=1647620975'
        }

response = requests.get(url=url, headers=headers, verify=False)
response.encoding="utf-8"
# 获取网页HTML代码
ata_obj = response.text
tree = etree.HTML(ata_obj)
aa=tree.xpath('/html/body/div[5]/div[2]/div/a')
# print(aa)
b=list=[]
for i in aa:
    b.append(i.xpath("./@href"))


print(str(b))