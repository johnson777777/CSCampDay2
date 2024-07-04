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
def Jump(image):
    """
    試試看有沒有其他判定方法
    可以讓小恐龍跳得更遠
    """
    for i in range(145,160):
        if image[125][i][0]==83:
            return True
    return False

if __name__=='__main__':
    # service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
    # driver = webdriver.Chrome(service=service)
    driver=webdriver.Chrome()
    driver.get(url)
    wait=WebDriverWait(driver, 10)
    _=wait.until(EC.presence_of_element_located((By.XPATH, "//html")),  'Error')
    _.send_keys(Keys.SPACE)

    while True:
        picture=wait.until(EC.presence_of_element_located((By.XPATH, "//canvas"))\
                        , 'Error').screenshot_as_png

        nparr = np.frombuffer(picture, np.uint8)
        image = cv.imdecode(nparr, cv.IMREAD_COLOR)
        if Jump(image):
            _=wait.until(EC.presence_of_element_located((By.XPATH, "//html")), 'Error')
            _.send_keys(Keys.SPACE)

    driver.quit()