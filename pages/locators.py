from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_LINK_SUBSTRING = "login"


class ProductPageLocators:
    ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME_H1 = (By.TAG_NAME, "h1")
    PRODUCT_PAGE_PRICE = (By.CSS_SELECTOR, ".price_color")
    ALERT_SUCCESS_PRICE = (By.CSS_SELECTOR, "#messages .alert-success:first-child strong")
    ALERT_INFO_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
