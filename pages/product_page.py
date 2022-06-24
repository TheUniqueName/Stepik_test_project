from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def product_names_should_match(self):
        product_name_h1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_H1).text
        product_name_alert = WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(ProductPageLocators.ALERT_SUCCESS_NAME)
        ).text
        assert product_name_h1 == product_name_alert, f"{product_name_h1} != {product_name_alert}"

    def product_prices_should_match(self):
        product_page_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_PRICE).text
        product_price_alert = WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(ProductPageLocators.ALERT_INFO_PRICE)
        ).text
        # time.sleep(60)
        assert product_page_price == product_price_alert, f"{product_page_price} != {product_price_alert}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message have not disappered, but should be"
