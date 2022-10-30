from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes= driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
    elif checkbox.get_attribute("value") == "option3":
        checkbox.click()


"""for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option3" and "option2":
        checkbox.click()
        break"""

"""for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option3":
        if checkbox.get_attribute("value") =="option2":
            checkbox.click()
            break
       # if checkbox.get_attribute("value") == "option2":"""