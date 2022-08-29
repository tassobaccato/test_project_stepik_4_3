from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# @pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8",
                                       #  "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
def test_guest_can_add_product_to_basket(browser):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    # link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                     # открываем страницу
    page.add_to_basket()            # нажимаем на кнопку добавить в корзину
    page.solve_quiz_and_get_code()  # решаем quiz
    page.message_product_in_basket()  # проверяем сообщение о добавлении товара в корзину
    page.name_of_product_in_basket()   # соответствует ли название добавленного товара товару в корзине
    page.message_basket_price()       # проверяем сообщение со стоимостью корзины
    page.compare_product_and_basket_price()  # совпадает ли стоимость корзины с ценой товара


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message2()
