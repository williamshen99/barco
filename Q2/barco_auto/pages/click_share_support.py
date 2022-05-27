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

    def get_result_detail(self):
        return self.get_element_text(*ClickShareSupportPageLocators.TEXT_RESULT_DETAIL)

    def get_validation_error_empty_char(self):
        return self.get_element_text(*ClickShareSupportPageLocators.TEXT_VALIDATION_ERROR_EMPTY_CHAR)

    def get_validation_error_min_chars_required(self):
        return self.get_element_text(*ClickShareSupportPageLocators.TEXT_VALIDATION_ERROR_MIN_CHARS_REQUIRED)

    def get_validation_error_wrong_format(self):
        return self.get_element_text(*ClickShareSupportPageLocators.TEXT_VALIDATION_ERROR_WRONG_FORMAT)

    def get_can_not_found_error(self):
        return self.get_element_text(*ClickShareSupportPageLocators.TEXT_CAN_NOT_FOUND_ERROR)
