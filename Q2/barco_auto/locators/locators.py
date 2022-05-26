from selenium.webdriver.common.by import By


class ClickShareSupportPageLocators(object):
    INPUT_SERIAL_NUMBER = (By.ID, "SerialNumber")
    BUTTON_GET_INFO = (By.CSS_SELECTOR, 'button[class^="btn btn-primary btn-block btn--icon btn--arrow"]')
    
    TEXT_RESULT_TITLE = (By.CSS_SELECTOR, 'h2[class^="c-result-tile__title"]')
    TEXT_RESULT_DETAIL = (By.CSS_SELECTOR, 'dl[class^="c-result-tile__dl"]')


    TEXT_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[class^="field - validation - error"]')
