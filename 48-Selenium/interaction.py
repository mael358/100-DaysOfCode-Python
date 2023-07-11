from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_driver_path = Service("C:\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path, options=options)
driver.maximize_window()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# articles_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "anyone can edit")
# all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# driver.get("http://secure-retreat-92358.herokuapp.com/")
#
# name_input = driver.find_element(By.NAME, "fName")
# lastName_input = driver.find_element(By.NAME, "lName")
# email_input = driver.find_element(By.NAME, "email")
# signup_button = driver.find_element(By.CSS_SELECTOR, "form button")
#
# name_input.send_keys("Marcos")
# lastName_input.send_keys("Velasquez")
# email_input.send_keys("marcosv200007@gmail.com")
# signup_button.click()

# //*[@id="langSelect-EN"]

driver.get("https://orteil.dashnet.org/cookieclicker/")

english_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')





