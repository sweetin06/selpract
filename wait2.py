import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(2) #a page will load
results = driver.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(3)
#parent component / child component
results = driver.find_elements_by_xpath("//div[@class='products']/div") #count of the searched results
count = len(results)
assert count > 0
for result in results:   #there is 3 results so we iterate them by loop
    result.find_element_by_xpath("div/button").click()

