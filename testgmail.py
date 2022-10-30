from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(executable_path="C:\\selenium browsers drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())
driver.get("https://google.com/")

#driver.find_element_by_id("identifier").send_keys("sweetintest22@gmail.com")

#driver.find_element_by_id()

loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
loginBox.send_keys("sweetintest22@gmail.com")

nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
nextButton[0].click()

passWordBox = driver.find_element_by_xpath(
    '//*[@id ="password"]/div[1]/div / div[1]/input')
passWordBox.send_keys("1Qazxsw2@")

nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
nextButton[0].click()

print('Login Successful...!!')'''


