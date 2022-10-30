from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
sort = []
driver.find_elements_by_xpath("//span[@text()='Veg/fruit name']")
veg = driver.find_elements_by_xpath("//tr/td[1]")
for ele in veg:
    sort.append(ele.text)

osort=sort.copy()
assert  sort == osort