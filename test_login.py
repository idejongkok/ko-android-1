from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from time import sleep
from page import LoginPage, HomePage, SuccessLoginPage
from data import Data
import pytest

def init_driver():
    options = UiAutomator2Options()
    options.udid = '127.0.0.1:62001'
    options.app_package = 'com.code2lead.kwad'
    options.app_activity = 'com.code2lead.kwad.MainActivity'
    options.platform_name = 'Android'
    options.auto_grant_permissions = True
    # options.no_reset = False
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',options=options)
    driver.implicitly_wait(10)
    
    return driver    

@pytest.fixture
def setup():
    driver = init_driver()
    yield driver
    driver.quit()

def test_login(setup):
    sleep(2)
    homepage = HomePage(setup)
    loginpage = LoginPage(setup)
    successpage = SuccessLoginPage(setup)
    
    homepage.click_login_button()
    loginpage.enter_username(Data.username)
    loginpage.enter_password(Data.password)
    loginpage.click_submit()
    sleep(2)
    submitbutton = successpage.check_text_submit_button()
    assert submitbutton == 'SUBMIT'

    
# def test_login_fail_username():
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',options=options)
#     driver.implicitly_wait(10)
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Btn6').click()
#     driver.find_element(AppiumBy.ID,'com.code2lead.kwad:id/Et4').send_keys('admin@gmail.')
#     driver.find_element(AppiumBy.ID,'com.code2lead.kwad:id/Et5').send_keys('admin123')
#     driver.find_element(AppiumBy.ID,'com.code2lead.kwad:id/Btn3').click()    
#     sleep(2)
#     error_message = driver.find_element(AppiumBy.ID,'com.code2lead.kwad:id/Tv8').text
    
#     assert error_message == 'Wrong Credentials'