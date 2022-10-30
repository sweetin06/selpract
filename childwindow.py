from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(2)
driver.find_element_by_link_text("Click Here").click()
wo=driver.window_handles          #it will take the all the windows which are open
driver.switch_to.window(wo[1])    #list is start from 0, so i select 1 , 2nd window
driver.close()