from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

# 目標：到好樂迪網站搜尋歌曲「怎麼了」
driver.get("https://www.holiday.com.tw/SongInfo/SongList.aspx?st=top&lt=tc")

# Todo: 填入正確的函數和值，注意以下程式碼是q3寫好的搬過來
search = driver.find_element(By.CLASS_NAME, "???")
search.clear() # 清空搜尋結果
search.send_keys("???")

time.sleep(2) # 停兩秒，時間可以自己改

button = driver.find_element(By.ID, "???")
button.send_keys(Keys.ENTER)

# Todo: 填入正確的函數和值
CrowdLu = driver.find_element(By.???, "盧廣仲")
CrowdLu.???
results = driver.find_elements(By.CLASS_NAME, "???")
for result in results:
    print(result.text)

# 以下程式碼不用動
time.sleep(10)
driver.quit()

