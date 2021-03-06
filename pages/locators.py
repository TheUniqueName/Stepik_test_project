from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_LINK_SUBSTRING = "login"
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    # REGISTER_SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME_H1 = (By.TAG_NAME, "h1")
    PRODUCT_PAGE_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_SUCCESS_NAME = (By.CSS_SELECTOR, "#messages .alert-success:first-child strong")
    ALERT_INFO_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items .row")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
