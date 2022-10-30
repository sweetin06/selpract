import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ch rome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5) #waiting
#driver.find_element_by_class_name("search-keyword").send_keys("bar")
results = driver.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements_by_xpath("//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element_by_xpath("div/button").click()
    #GET IT FROM PARENT ELEMENT
    driver.find_element_by_css_selector("promocode").send_keys("sweetin")
    driver.find_element_by_css_selector("promoBtn").click()
    time.sleep(4)
    print(driver.find_elements_by_class_name("promoInfo").text)