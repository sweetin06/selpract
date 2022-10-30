from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_class_name("search-keyword").send_keys("ber")
#a.submit()
time.sleep(2)
results = driver.find_elements_by_xpath("//div[@class='products']/div") #for select the all sorted item
#results = driver.find_elements_by_xpath("//div[@class='products']/div[1]") #for selecting the one item from the sorted list
print(len(results))# count of searched items
#assert results > 0 #a result should be grater than of 0
for result in results:   #there is 3 results so we iterate them by loop
    result.find_element_by_xpath("div/button").click() #chaining
#to select the img css -> alt for to click the cart icon
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click() #a button's text was paassed
#to execute the promo code text box
#driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")