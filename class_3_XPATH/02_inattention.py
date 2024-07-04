from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import cv2 as cv
import numpy as np
import time

url='https://www.holiday.com.tw/SongInfo/SongList.aspx?st=top&lt=tc'
if __name__=='__main__':
    service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service)
    #driver=webdriver.Chrome()
    driver.get(url)
    wait=WebDriverWait(driver, 10)

    # 定位搜尋的輸入框
    searchXPATH="__???__"
    search=wait.until(EC.presence_of_element_located((By.XPATH, searchXPATH)), 'Error')
    search."__???__"("__???__")

    # 定位按鈕
    buttonXPATH="__???__"
    button=wait.until(EC.presence_of_element_located((By.XPATH, buttonXPATH)), "Error")
    button.click()

    # 定位曲號
    numberXPATH="__???__"
    number=wait.until(EC.presence_of_element_located((By.XPATH, numberXPATH)), "Error")
    print(number.text)

    driver.quit()