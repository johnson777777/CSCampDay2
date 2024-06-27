from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://kktix.com/")

# kktix 帳號：exhaustedohh@gmail.com
# kktix 密碼：iamhungry

# TODO
# Step 1: 找到登入按鍵並點擊
sign = driver.find_elements(By.__1__, "__2__")
__3__

# Step 2: 填入帳號密碼
signin_account = driver.find_element(By.NAME, "__4__")
signin_account.send_keys("__5__")
signin_password = driver.find_element(By.NAME, "__6__")
signin_password.send_keys("__7__" + Keys.__8__) 

# Step 3: 搜尋「wannasleep」演唱會
element = driver.find_element(By.NAME, "__9__")
__10__ # 清除輸入結果
element.send_keys("__11__" + Keys.ENTER)

# Step 4: 找到 7/12 桃園場
link = driver.find_element(By.__12__, "__13__")
__14__
next_step = driver.find_elements(By.CLASS_NAME, "__15__")
next_step[__16__].click()

# Step 5: 顯示五秒並關閉瀏覽器
time.sleep(__17__)
driver.quit()


