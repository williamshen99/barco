from selenium.webdriver.common.by import By


class ClickShareSupportPageLocators(object):
    INPUT_SERIAL_NUMBER = (By.ID, "SerialNumber")
    BUTTON_GET_INFO = (By.CSS_SELECTOR, 'button[class^="btn btn-primary btn-block btn--icon btn--arrow"]')
    
    TEXT_RESULT_TITLE = (By.CSS_SELECTOR, 'h2[class^="c-result-tile__title"]')
    TEXT_RESULT_DETAIL = (By.CSS_SELECTOR, 'dl[class^="c-result-tile__dl"]')

    TEXT_VALIDATION_ERROR_EMPTY_CHAR = (By.CSS_SELECTOR, 'span.field-validation-error:nth-child(3)')
    TEXT_VALIDATION_ERROR_MIN_CHARS_REQUIRED = (By.CSS_SELECTOR, 'span[data-bind^="visible: showIsTooShort"]')
    TEXT_VALIDATION_ERROR_WRONG_FORMAT = (By.CSS_SELECTOR, 'span[data-bind^="visible: showIsWrongFormat"]')
    TEXT_CAN_NOT_FOUND_ERROR = (By.XPATH, '/html/body/div[1]/div[2]/section/div/div[2]/div/div/div/div')
