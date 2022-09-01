from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "product is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "empty basket message is not presented"

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            "empty basket message is presented, but should not be"

    def empty_basket_message_is_disappeared(self):
        assert self.is_disappeared(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            "empty basket message is disappeared"
