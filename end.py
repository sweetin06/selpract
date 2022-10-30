import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#a is tag name , contains is a class name, href is a attribute, shop is  value
driver.find_element_by_css_selector("a[href*='shop'").click()
products=driver.find_elements_by_xpath("//div[@class='card h-100' ]")
for product in products:
    prodname=product.find_elements_by_xpath("div/h4/a").text
    if prodname== "Balackberry":
        product.find_elements_by_css_selector(".card-footer button")[i].click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_elements_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
#wait= WebDriverWait(driver, 10)
#wait.until(expected_conditions.presence_of_element_located_by_linktext )
element = WebDdriverWait(driver,10).until(driver.find_element_by_link_text("INDIA"))