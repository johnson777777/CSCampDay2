from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

# 目標：自己點手好痠而且好慢，希望電腦可以自動連續點貓貓

driver.get("https://popcat.click")
driver.fullscreen_window() # 全螢幕顯示

# TODO: 填入正確的函數
cat = driver.find_element(By.ID, "???")

while True:
    cat.click()

# 用 for 迴圈設定點擊次數（要用的話記得把上面的 while 迴圈註解掉）
for i in range(10): # 可以自行調整點擊次數
    cat.click()
    
driver.quit() # 關掉瀏覽器
