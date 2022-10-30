from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#mouse events

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
#type action chains and import the packages
action =ActionChains(driver)
#actions pre built functions
#action.double_click()
#action.context_click()
#action.drag_and_drop()
#to complete the actions with perform
action.move_to_element(driver.find_element_by_id("mousehover")).perform()
action.context_click(driver.find_element_by_link_text("Top")).perform()
action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()