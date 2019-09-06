# -*- coding: utf-8 -*-
__Author__ = "hsingpu"
__Date__ = "2019/5/19"

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import ImageGrab

options = webdriver.ChromeOptions()
# options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option('excludeSwitches', ['enable-automation'])


# driver = webdriver.Chrome(executable_path=r'F:\全栈21期\day104爬虫\day04\chromedriver.exe',chrome_options=options)
driver = webdriver.Chrome(executable_path=r'F:\全栈21期\day104爬虫\chromedriver_win3276\chromedriver.exe',)
driver.get('http://www.baidu.com')
sleep(2)

driver.find_element_by_tag_name('html').send_keys(Keys.CONTROL+Keys.SHIFT+'j')
# builder = ActionChains(driver)
# builder.key_down(Keys.F12).perform()
# builder.key_up(Keys.F12).perform()
# builder.key_down(Keys.CONTROL+']').perform()
while True:
    sleep(5)
    # builder.key_down(Keys.F5).perform()
    driver.refresh()
    # driver.save_screenshot('shortcut.png')
    im=ImageGrab.grab()
    im.save(r'./shortcut.png')
    #发送邮件接口
# driver.quit()
