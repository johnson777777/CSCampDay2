from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

# 目標：自己點手好痠而且好慢，希望電腦可以自動連續點貓貓

# TODO: 填入正確的函數
driver.get("https://popcat.click")

cat = driver.find_element(By.ID, "__1__")
while True:
    cat.__2__


