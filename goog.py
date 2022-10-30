from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\selenium browsers drivers\\chromedriver.exe")

driver.get("https://www.google.com/")
search=driver.find_element_by_name("q")
search.send_keys("automation testing")
search.submit()