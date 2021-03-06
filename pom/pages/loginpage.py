from pom.locator.locator import Locator

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locator.username_textbox_id
        self.password_textbox_id = Locator.password_textbox_id
        self.login_button = Locator.login_button

    def enter_username(self,):
        self.driver.find_element_by_id("self.username_textbox_id").clear()
        self.driver.find_element_by_id("self.username_textbox_id").send_keys("username")

    def enter_password(self):
        self.driver.find_element_by_id("self.password_textbox_id").clear()
        self.driver.find_element_by_id("self.password_textbox_id").send_keys("password")

    def click_login(self):
        self.driver.find_element_by_id("self.login_button").click()
