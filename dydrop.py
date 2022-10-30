import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
#sleep
time.sleep(2)
#identified by class name
countries=driver.find_elements_by_class_name("ui-menu-item")
#countries = driver.find_elements_by_css_selector("li[class ='ui-menu-item']a")
print(len(countries))
#search the count in list
for country in countries:
    if country.text == "India":   #select the equvalant text
        country.click()           #select
        break                     #use break for exit the loop
