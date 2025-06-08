import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = selenium.webdriver.Chrome()
# Navigate to the URL
query = "laptop"
driver.get(f"https://www.amazon.com/s?k={query}")

elem = driver.find_elements(By.CLASS_NAME, "puis-card-container")
print(elem.text)

time.sleep(3)
driver.close