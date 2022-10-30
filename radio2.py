from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radios= driver.find_elements_by_xpath("//input[@type='radio']")

for radiobtn in radios:
    if radiobtn.get_attribute("value") == "radio3":
       # if checkbox.get_attribute("value") == "option2":
       radiobtn.click()
       break

