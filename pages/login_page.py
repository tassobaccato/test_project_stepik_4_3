from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # assert True , Конструкция 'Name' in s возвращает просто True или False
        assert "login" in self.browser.current_url, "'login' is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # assert True
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM, "Login form is not presented")

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # assert True
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM, "Register form is not presented")
