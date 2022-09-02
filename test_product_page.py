from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import pytest
import time

promo_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"


# @pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail),
# "8", "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):

def test_guest_can_add_product_to_basket(browser):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    # link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, promo_link)  #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                     # открываем страницу
    page.add_to_basket()            # нажимаем на кнопку добавить в корзину
    page.solve_quiz_and_get_code()  # решаем quiz
    page.message_product_in_basket()  # проверяем сообщение о добавлении товара в корзину
    page.name_of_product_in_basket()   # соответствует ли название добавленного товара товару в корзине
    page.message_basket_price()       # проверяем сообщение со стоимостью корзины
    page.compare_product_and_basket_price()  # совпадает ли стоимость корзины с ценой товара


@pytest.mark.xfail(reason="it is a negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="it is a negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason="login link is invalid")
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket()
    page.should_not_be_product()
    page.should_be_empty_basket_message()


@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, promo_link)
        self.page.open()
        self.page.go_to_valid_login_link()
        self.page.register_new_user()
        time.sleep(5)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.page = ProductPage(browser, promo_link)
        self.page.open()
        self.page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        self.page = ProductPage(browser, promo_link)
        self.page.open()
        self.page.add_to_basket()
        self.page.solve_quiz_and_get_code()
        self.page.message_product_in_basket()
        self.page.name_of_product_in_basket()
        self.page.message_basket_price()
        self.page.compare_product_and_basket_price()

#  pytest -s test_product_page.py
