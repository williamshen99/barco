from pages.base import BasePage
from locators.locators import ClickShareSupportPageLocators
from testdata.test_serial_numbers import test_serial_numbers


class ClickShareSupportPage(BasePage):
    
    def open_page(self, url):
        self.navigate(url)

    def input_serial_number(self, keys=test_serial_numbers['valid']['with_warranty']['serial_number']):
        self.input_keys(keys, *ClickShareSupportPageLocators.INPUT_SERIAL_NUMBER)

    def click_get_info_button(self):
        self.click_element(*ClickShareSupportPageLocators.BUTTON_GET_INFO)

    def wait_for_result_title(self):
        self.wait_for_element(*ClickShareSupportPageLocators.TEXT_RESULT_TITLE)

    def wait_for_result_detail(self):
        self.wait_for_element(*ClickShareSupportPageLocators.TEXT_RESULT_DETAIL)

    def get_result_detail(self):
        return self.get_element_text(*ClickShareSupportPageLocators.TEXT_RESULT_DETAIL)


"""
class AmazonLoginPage(BasePage):

    def input_account_info(self, keys=test_accounts['valid']['account']):
        self.input_keys(keys, *AmazonLoginPageLocators.INPUT_ACCOUNT_COLUMN)
        
    def click_continue_button(self):
        self.click_element(*AmazonLoginPageLocators.CONTINUE_BUTTON)

    def input_password(self, keys=test_accounts['valid']['password']):
        self.input_keys(keys, *AmazonLoginPageLocators.INPUT_PASSWORD_COLUMN)

    def click_login_button(self):
        self.click_element(*AmazonLoginPageLocators.LOGIN_BUTTON)

    def click_logout_button(self):
        self.click_element_not_interactable(*AmazonLoginPageLocators.LOGOUT_TEXT)

    def get_login_err(self):
        self.get_element_text(*AmazonLoginPageLocators.LOGIN_ERR_TEXT)
"""