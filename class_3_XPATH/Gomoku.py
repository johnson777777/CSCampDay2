from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import cv2 as cv
import numpy as np
import time
import random as rd
url='https://papergames.io/zh/%E4%BA%94%E5%AD%90%E6%A3%8B'
def play():
    """
    主要修改區塊-2
    """
    try:
        unclicks=wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td[contains(@class,'clickable')]")), 'Er')
        unclicks[rd.randint(0,len(unclicks)-1)].click()
        return True
    except:
        return False

if __name__=='__main__':
    # service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
    # driver = webdriver.Chrome(service=service)
    driver=webdriver.Chrome()
    driver.get(url)
    wait=WebDriverWait(driver, 10)

    # 點擊對戰按鈕
    fight=wait.until(EC.presence_of_element_located((By.XPATH, "/html/body[@class='d-flex flex-column dark']/app-root[@class='flex-grow-1 overflow-auto']/app-navigation/div[@class='d-flex h-100']/div[@class='d-flex flex-column h-100 w-100']/main[@class='flex-grow-1 overflow-auto viewport-dense']/app-game-landing[@class='ng-star-inserted']/div[@class='container-fluid ng-star-inserted']/div[@class='row dashboard pt-md-2 pt-md-5 bg-gray-000']/div[@class='col-md-12 col-lg-6 p-0 d-md-flex flex-column align-items-center']/div/div[@class='game-pad container-small']/div[@class='pad box-shadow-1 bg-light d-md-flex flex-column ng-star-inserted']/div[@class='pad-content']/div[@class='game-actions']/button[@class='btn btn-outline-dark mb-2 ng-star-inserted']")),  'Error')
    fight.click()

    # 輸入暱稱
    nickname=wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mat-mdc-dialog-0']/div/div/app-guest-registration-dialog/form/app-dialog-layout/section/div/div/input")),  'Error')
    nickname.send_keys('123')

    time.sleep(1)
    # 點擊確認按紐
    confirm=driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/app-guest-registration-dialog/form/app-dialog-layout/footer/button')
    confirm.click()

    # 點擊繼續
    conti=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-mdc-dialog-1"]/div/div/app-game-settings-dialog/form/app-dialog-layout/footer/button')), 'error')
    conti.click()
    
    
    # 一直下 不要停
    """
    主要修改區塊-1
    """
    playing=True
    while playing:
        playing=play()
    
    driver.quit()