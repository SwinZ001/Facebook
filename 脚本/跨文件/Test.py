from time import sleep

import openpyxl as openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

bro = webdriver.Chrome(executable_path='F:\python\python3.9.10\Scripts\chromedriver.exe')
bro.get("https://business.facebook.com/settings/ad-accounts/925247497960475?business_id=2772277696222403")
bro.find_element_by_xpath('//*[@id="email"]').send_keys("geoffrey.rupiah")
bro.find_element_by_xpath('//*[@id="pass"]').send_keys("swinz.ab456")
bro.find_element_by_xpath('//*[@id="loginbutton"]').click()
bro.implicitly_wait(30)
# bro.find_elements_by_class_name()
aa=bro.find_element_by_xpath('//*[@id="biz_settings_content_view"]/div/div[4]/div[2]/div/div[3]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div').find_elements_by_class_name("ellipsis")
for el in aa:
    print(el.text)

