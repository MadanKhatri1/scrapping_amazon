from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()
query="laptop"

for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=ZMI68NQ42PUE&sprefix=laptop%2Caps%2C243&ref=nb_sb_noss_1")

    element=driver.find_elements(By.CLASS_NAME,"puis-card-container")

    print(element)
    print(f"{len(element)} items found")

    for elems in element:
        print(elems.text)

    time.sleep(8)
    driver.close()