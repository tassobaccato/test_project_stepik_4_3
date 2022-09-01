from selenium.webdriver.common.by import By


class ProductPageLocators(object):
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner")
    NAME_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div>h1")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner>p")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_PRICE = (By.TAG_NAME, "h1+p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_VIEW_BASKET = (By.CSS_SELECTOR, "span>a.btn.btn-default")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators(object):
    FIELD_REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    FIELD_REGISTRATION_PASS1 = (By.ID, "id_registration-password1")
    FIELD_REGISTRATION_PASS2 = (By.ID, "id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")



