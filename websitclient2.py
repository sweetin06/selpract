from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element_by_link_text("Forgot password?").click()
driver.find_element_by_xpath("//input[@type='email']").send_keys("sw@gmail.com")
driver.find_element_by_xpath("//input[@id='userPassword']").send_keys("1Qaz")
driver.find_element_by_xpath("//input[@id='confirmPassword']").send_keys("1Qazxsw2@")
driver.find_element_by_xpath("//button[@type='submit']").click()
#driver.find_element_by_id("userPasword").send_keys("1Qazxsw2@")
#driver.find_element_by_id("confirmPassword").send_keys("1Qazxsw2@")