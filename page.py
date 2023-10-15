# from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from locator import *

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        
    def click_login_button(self):
        self.driver.find_element(AppiumBy.XPATH, locatorHomepage.login_button).click()
        

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
    
    def enter_username(self,username):
        self.driver.find_element(AppiumBy.ID, locatorLoginpage.username_input).send_keys(username)
    
    def enter_password(self,password):
        self.driver.find_element(AppiumBy.ID, locatorLoginpage.password_input).send_keys(password)
    
    def click_submit(self):
        self.driver.find_element(AppiumBy.ID, locatorLoginpage.submit_button).click()
        
class SuccessLoginPage:
        def __init__(self,driver):
            self.driver = driver
            
        def check_text_submit_button(self):
            text= self.driver.find_element(AppiumBy.ID, locatorSuccesspage.submit_button).text
            return text