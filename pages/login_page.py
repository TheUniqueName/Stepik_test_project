from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        substr_position = self.browser.current_url.find(LoginPageLocators.LOGIN_LINK_SUBSTRING)
        assert substr_position > -1, f"There is no '{LoginPageLocators.LOGIN_LINK_SUBSTRING}' substring in current URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email = email or (str(time.time()) + "@fakemail.org")  # Если в качестве email передана пустая строка, то генерируем email сами
        password = password or str(time.time())  # Если в качестве password передана пустая строка, то генерируем password сами
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_input.send_keys(email)  # Заполняем емейл
        password_1_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_1_input.send_keys(password)  # Заполняем пароль
        password_2_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM)
        password_2_input.send_keys(password, Keys.RETURN)  # Заполняем подтверждение пароля и жмем на Return, т.е. на ненамовский Enter
