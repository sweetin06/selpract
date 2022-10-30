import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup"):
class testone():
        def test2(self,setup):


"""options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#get the url
driver.get("https://rahulshettyacademy.com/angularpractice/")"""
        self.driver.find_element_by_name("name").send_keys("SWEETIN AALESTA")
        self.driver.find_element_by_name("email").send_keys("sw@gmail.com")
        self.driver.find_element_by_id("exampleInputPassword1").send_keys("1Qazxsw2@")
#select the check box
        self.driver.find_element_by_class_name("form-check-input").click()
#select the dropdown
        dn = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        dn.select_by_index(1)
#ch = Select(driver.find_element_by_id("inlineRadio2")).Select()
#select the radio button
        self.driver.find_element_by_xpath("//input[@value='option2']").click()
#select a date
        self.driver.find_element_by_name("bday").send_keys("06062000")
#xpath as type for button click
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
#msg = driver.find_element_by_class_name("alert-success").text
#assert "Success" in msg
