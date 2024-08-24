from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=3EPZEOHF4YL4G&sprefix=laptop%2Caps%2C226&ref=nb_sb_noss_1")

element=driver.find_element(By.CLASS_NAME,"puis-card-container")

print(element.get_attribute("outerHTML"))

time.sleep(8)
driver.close()