# -*- coding: utf-8 -*-
__Author__ = "hsingpu"
__Date__ = "2019/5/19"

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import ImageGrab
from send2alimail import sendmail

#============================打开浏览器开发者模式===========================
options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
# options.add_experimental_option('excludeSwitches', ['enable-automation'])


driver = webdriver.Chrome(executable_path=r'..\libs\chromedriver.exe',chrome_options=options)
# driver = webdriver.Chrome(executable_path=r'F:\全栈21期\day104爬虫\chromedriver_win3276\chromedriver.exe',)
driver.get('http://www.qq.com')
sleep(1)

# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.SHIFT+'j')
builder = ActionChains(driver)
# builder.send_keys('test')
# builder.key_down(Keys.CONTROL).send_keys('a')
# builderx = ActionChains(driver)
# builder.key_down(Keys.CONTROL).send_keys(']')
# builder.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('j').key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()
# builder.key_down(Keys.F12).perform()
# builder.key_up(Keys.F12).perform()
# builder.key_down(Keys.CONTROL+']').perform()
builder.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('j').perform()
def run():
    while True:
        sleep(5)
        # builder.key_down(Keys.F5).perform()
        driver.refresh()
        # driver.save_screenshot('shortcut.png')
        #=========================截图========================
        im = ImageGrab.grab()
        im.save(r'./shortcut.png')


        # ===============发送邮件接口===========================
        # sendmail()


# driver.quit()

if __name__ == '__main__':
    run()