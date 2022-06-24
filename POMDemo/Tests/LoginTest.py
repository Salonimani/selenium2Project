from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POMDemo.Pages.LoginPage import LoginPage
from POMDemo.Pages.HomePage import Homepage
import htmltestrunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Service('C:/Users/umang/Downloads/chromedriver_win32/chromedriver.exe')
        cls.driver = webdriver.Chrome(service= cls.s)
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_Login()

        homepage = Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element(by=By.ID, value="txtUsername").send_keys("Admin")
        # self.driver.find_element(by=By.ID, value="txtPassword").send_keys("admin123")
        # self.driver.find_element(by=By.ID, value="btnLogin").click()
        # self.driver.find_element(by=By.ID, value="welcome").click()
        # self.driver.find_element(by=By.LINK_TEXT, value="Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner= htmltestrunner.htmltestrunner(output='C:/Users/umang/PycharmProjects/selenium2/Reports'))

