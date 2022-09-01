from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def message_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_BASKET), "product is not in basket"

    def name_of_product_in_basket(self):
        name_of_product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_BASKET).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert name_of_product_in_basket == product_name, "it is not my product"

    def message_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_PRICE), "message is missing"

    def compare_product_and_basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_price == product_price, "prices do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared"

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "product is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "empty basket message is not presented"


