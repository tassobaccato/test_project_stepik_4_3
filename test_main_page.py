from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import pytest

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_product()
    page.should_be_empty_basket_message()


@pytest.mark.xfail(reason="it is a negative test")
def test_guest_cant_see_empty_basket_message_in_empty_basket(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_empty_basket_message()


@pytest.mark.xfail(reason="it is a negative test")
def test_empty_basket_message_is_disappeared(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.empty_basket_message_is_disappeared()


@pytest.mark.login_guest        # pytest -m login_guest test_main_page.py
class TestLoginFromMainPage(object):
    @pytest.mark.xfail(reason="invalid link")
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

# pytest -s test_main_page.py
# pytest -m login_guest test_main_page.py
