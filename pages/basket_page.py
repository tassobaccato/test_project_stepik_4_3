from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators


class BasketPage(BasePage):
    def go_to_basket(self):
        btn_view_basket = self.browser.find_element(*BasePageLocators.BTN_VIEW_BASKET)
        btn_view_basket.click()
        # return BasketPage(browser=self.browser, url=self.browser.current_url)

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "product is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "empty basket message is not presented"
