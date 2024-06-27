from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

# kktix 帳號：exhaustedohh@gmail.com
# kktix 密碼：iamhungry

driver.get("https://kktix.com/")

# 登入
sign = driver.find_elements(By.???, "???")
???
sign_account = driver.find_element(By.NAME, "???")
sign_account.send_keys("???")
sign_password = driver.find_element(By.NAME, "???")
sign_password.send_keys("i???" + Keys.???)

# 查詢演唱會場次
element = driver.find_element(By.NAME, "???")
??? # 清除輸入結果
element.send_keys("???" + Keys.ENTER)
link = driver.find_element(By.???, "???")
???
next_step = driver.find_elements(By.CLASS_NAME, "???")
next_step[???].click()
print("success")

time.sleep(???)
driver.quit() #關閉瀏覽器

