from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path=r'..\libs\chromedriver.exe')

browser.get('http://www.baidu.com')
#assert 'Yahoo' in browser.title
time.sleep(2)
elem = browser.find_element(By.ID, 'kw')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

time.sleep(4)
browser.quit()