from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

# 目標：印出好樂迪國語點播排行榜前20名歌曲＆歌手

driver.get("https://www.holiday.com.tw/SongInfo/SongList.aspx?st=top&lt=tc")

# Todo: 填入正確的函數和值
numbers = driver.find_elements(By.???, "???")
titles = driver.find_elements(By.???, "???")
singers = driver.find_elements(By.???, "???")

# 以下程式碼不用動
for i in range(0, 20):
    print(numbers[i+1].text, titles[i].text, singers[i].text)

time.sleep(10)
driver.quit()

