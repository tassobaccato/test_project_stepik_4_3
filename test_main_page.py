from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_product()
    page.should_be_empty_basket_message()
