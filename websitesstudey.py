#test the website
from select import select
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\selenium browsers drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("sweetin aalesta") #sucess


driver.find_element_by_name("email").send_keys("sw@devaxcel.com") #sucess

driver.find_element_by_id("exampleInputPassword1").send_keys("1Qazxsw2@") #sucess
driver.find_element_by_class_name("form-check-input").click()
#static dropdown
#download the select package
dn = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dn.select_by_index(1)
#dropdown.select_by_index(1)
#dropdown.select


