#News Aggregator
#dzul.aiman@Gmail.com
#2023-10-14

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#1. crawl web page, and grab data
def crawl():
    thenews = []
    driver = webdriver.Chrome()
    driver.get("https://www.bharian.com.my/sukan")
    time.sleep(3)
    elem = driver.find_elements(By.CLASS_NAME, "field-title")
    for item in elem:
        print(item.text)
        thenews.append(item.text)
    time.sleep(10)
    driver.close()

    return thenews
