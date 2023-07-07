from selenium.webdriver.chrome.service import Service
from selenium import webdriver


chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://amazon.com")

driver.close()
