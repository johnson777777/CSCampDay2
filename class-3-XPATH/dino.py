from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import cv2 as cv
import numpy as np
import time

url='https://trex-runner.com/'
if __name__=='__main__':
    service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service)
    # driver=webdriver.Chrome()
    driver.get(url)
    wait=WebDriverWait(driver, 10)
    _=wait.until(EC.presence_of_element_located((By.XPATH, "/html")), 'Error')
    _.send_keys(Keys.SPACE)

    
    while True:
        picture=wait.until(EC.presence_of_element_located((By.XPATH, "//canvas"))\
                           , 'Error').screenshot_as_png
        # img=cv.imread(aa)
        nparr = np.frombuffer(picture, np.uint8)
        image = cv.imdecode(nparr, cv.IMREAD_COLOR)

        if image[125][135][0]==83:
            _=wait.until(EC.presence_of_element_located((By.XPATH, "/html")), 'Error')
            _.send_keys(Keys.SPACE)

    driver.close()
