from POMDemo.Locators.locators import Locators
from selenium.webdriver.common.by import By
class LoginPage():

    def __init__(self,driver):
        self.driver= driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.Login_button_id     = Locators.Login_button_id

    def enter_username(self, username):
        self.driver.find_element(by= By.ID, value= self.username_textbox_id).clear()
        self.driver.find_element(by= By.ID, value= self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(by= By.ID, value= self.password_textbox_id).clear()
        self.driver.find_element(by= By.ID, value= self.password_textbox_id).send_keys(password)

    def click_Login(self):
        self.driver.find_element(by= By.ID, value= self.Login_button_id).click()


