from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url="https://kma.kkbox.com/charts/yearly/newrelease?cate=314&lang=tc&terr=tw"

if __name__=='__main__':
    service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    driver.implicitly_wait(10)
    songs=driver.find_elements(By.XPATH, "//span[@class='charts-list-song']")
    for song in songs:
        print(song.text)
    driver.close()
