from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_id("name").send_keys("name")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

alert.accept() #confrim
#alert.dismiss()   # cancel