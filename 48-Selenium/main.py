from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = Service("C:\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")
# driver.get("https://www.amazon.com/-/es/Instant-Pot-IP-DUO60-6cuartos-1000W/dp/B06Y1YD5W7/ref=sr_1_3?__mk_es_US=%C3"
#            "%85M%C3%85%C5%BD%C3%95%C3%91&crid=38MK3RDCIYKYS&keywords=instant+pot&qid=1689113644&sprefix=instant+pot"
#            "%2Caps%2C201&sr=8-3")
# values = driver.find_element(By.ID, "attach-base-product-price")
# print(values.get_attribute('value'))
# driver.quit()

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

# for name in event_names:
#     print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)


driver.close()
