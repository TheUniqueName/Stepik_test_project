from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def get_product_name_h1(self):
        product_name_h1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_H1).text
        return product_name_h1

    def get_product_name_alert(self, browser):
        product_name_alert = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located(ProductPageLocators.ALERT_SUCCESS_PRICE)
        ).text
        return product_name_alert

    def get_product_page_price(self):
        product_page_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_PRICE).text
        return product_page_price

    def get_product_price_alert(self, browser):
        product_price_alert = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located(ProductPageLocators.ALERT_INFO_PRICE)
        ).text
        return product_price_alert

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message have not disappered, but should be"
