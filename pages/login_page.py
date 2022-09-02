from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self):
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_EMAIL).send_keys(str(time.time()) + '@fakemail.org')
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_PASS1).send_keys("mko2559nji26")
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_PASS2).send_keys("mko2559nji26")
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()




