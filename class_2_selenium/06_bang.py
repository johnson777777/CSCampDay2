from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 目標：印出好樂迪國語點播排行榜前20名歌曲＆歌手

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.holiday.com.tw/SongInfo/SongList.aspx?st=top&lt=tc")
driver.fullscreen_window() # 全螢幕顯示

# 捲動頁面
for i in range(10):
    driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(1)

# TODO: 填入正確的值
numbers = driver.find_elements(By.CLASS_NAME, "???")
titles = driver.find_elements(By.CLASS_NAME, "???")
singers = driver.find_elements(By.CLASS_NAME, "???")

# 印出前20名排行榜結果
for i in range(0, 20):
    print(numbers[i+1].text, titles[i].text, singers[i].text)

driver.quit()
