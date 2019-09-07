# -*- coding: utf-8 -*-
__Author__ = "hsingpu"
__Date__ = "2019/5/19"

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import ImageGrab
from send2alimail import sendmail

options = webdriver.FirefoxOptions()
options.add_argument("--auto-open-devtools-for-tabs")
# options.add_experimental_option('excludeSwitches', ['enable-automation'])


# driver = webdriver.Chrome(executable_path=r'F:\全栈21期\day104爬虫\day04\chromedriver.exe',chrome_options=options)
driver = webdriver.Firefox(executable_path=r'D:\Program Files\Firefox\geckodriver.exe',firefox_options=options)
driver.get('http://www.baidu.com')
sleep(2)
# driver.find_element_by_tag_name('body')

# driver.find_element_by_tag_name('body').send_keys(Keys + Keys.SHIFT + 'i')

builder = ActionChains(driver)
# builder.send_keys('test__').perform()
sleep(1)
# builder = ActionChains(driver)
builder.key_down(Keys.CONTROL).send_keys(']').perform()

# builder.key_down(Keys.SHIFT).send_keys('a').perform()
# builder.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down('i').key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()
# builder.send_keys(Keys.CONTROL + Keys.SHIFT + 'i')


# builder.key_down(Keys.F12).perform()
# builder.key_up(Keys.F12).perform()
# builder.key_down(Keys.CONTROL+']').perform()
def run():
    while True:
        sleep(5)
        # builder.key_down(Keys.F5).perform()
        driver.refresh()
        # driver.save_screenshot('shortcut.png')
        im = ImageGrab.grab()
        im.save(r'./shortcut.png')


        # 发送邮件接口
        # sendmail()


# driver.quit()

if __name__ == '__main__':
    run()
