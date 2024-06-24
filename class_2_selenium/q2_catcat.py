from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

# 目標：自己點手好痠而且好慢，希望電腦可以自動連續點貓貓

# Todo: 填入正確的函數
driver.???("https://popcat.click")

cat = driver.find_element(By.ID, "app")
while True:
    cat.???


