from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.ptt.cc/bbs/Japan_Travel/index.html")

element = driver.find_element(By.CLASS_NAME, "query") 
element.clear() # 清除輸入結果
element.send_keys("北海道" + Keys.ENTER)
elements = driver.find_elements(By.CLASS_NAME, "title")
for element in elements:
    print(element.text)

time.sleep(5)
driver.quit() # 關閉瀏覽器