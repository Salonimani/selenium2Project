from selenium import webdriver
from selenium.webdriver.common.by import By
from POMDemo.Locators.locators import Locators
class Homepage():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_welcome(self):
        self.driver.find_element(by= By.ID, value= self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(by= By.LINK_TEXT, value= self.logout_link_linkText).click()
