from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://kktix.com/")
driver.fullscreen_window() # 全螢幕顯示

# kktix 帳號：exhaustedohh@gmail.com
# kktix 密碼：iamhungry

# TODO: 填入正確的函數或值
# Step 1: 找到登入按鍵並點擊
sign = driver.find_elements(By.CLASS_NAME, "???") # 找到登入按鍵
sign[1].click() # 點擊登入按鍵

# Step 2: 填入帳號密碼
signin_account = driver.find_element(By.NAME, "user[login]")
signin_account.send_keys("???") # 填入帳號
signin_password = driver.find_element(By.NAME, "user[password]")
signin_password.send_keys("???" + Keys.ENTER) # 填入密碼
 
# Step 3: 搜尋「wannasleep」演唱會
element = driver.find_element(By.NAME, "???") # 找到搜尋框
element.clear() # 清除輸入結果
element.send_keys("???" + Keys.ENTER) # 輸入並搜尋

# Step 4: 找到 7/12 桃園場
link = driver.find_element(By.PARTIAL_LINK_TEXT, "7/12") # 搜尋 7/12 桃園場連結
link.click() # 點擊 7/12 桃園場連結
next_step = driver.find_elements(By.CLASS_NAME, "???") # 找到下一步的按鈕
next_step[2].click() # 點擊下一步的按鈕

# Step 5: 顯示五秒並關閉瀏覽器
time.sleep(5) # 等待五秒
driver.quit() # 關閉瀏覽器


