from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self):
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_EMAIL).send_keys("tester@mail.ru")
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_PASS1).send_keys("123456789")
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_PASS2).send_keys("123456789")
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()




