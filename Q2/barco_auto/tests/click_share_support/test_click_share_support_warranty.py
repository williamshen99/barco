from testdata.test_serial_numbers import test_serial_numbers


class TestClickShareSupportWarranty:

    def test_get_warranty_normally(self, go_to_click_share_support_page):

        click_share_support = go_to_click_share_support_page
        click_share_support.input_serial_number()
        click_share_support.click_get_info_button()
        click_share_support.wait_for_result_title()

        result_detail = click_share_support.get_result_detail()
        result_detail_list = result_detail.split('\n')

        for idx in range(0, len(result_detail_list) - 1, 2):
            result_item = result_detail_list[idx]
            result_value = result_detail_list[idx+1]

            if result_item not in test_serial_numbers['valid']['with_warranty'].keys():
                raise ValueError(f'unexpected response attribute: {result_item}')
            assert test_serial_numbers['valid']['with_warranty'][result_item] == result_value

    def test_get_warranty_with_no_warranty_number(self, go_to_click_share_support_page):

        click_share_support = go_to_click_share_support_page
        click_share_support.input_serial_number(keys=test_serial_numbers['invalid']['no_warranty'])
        click_share_support.click_get_info_button()
        click_share_support.wait_for_result_title()

        error_message = click_share_support.get_can_not_found_error()
        assert error_message == "We couldn't find a product with this serial number. Please double-check the serial number and try again."

    def test_get_warranty_with_empty_char(self, go_to_click_share_support_page):

        click_share_support = go_to_click_share_support_page
        click_share_support.input_serial_number(keys=test_serial_numbers['invalid']['empty_char'])
        click_share_support.click_get_info_button()
        click_share_support.wait_for_result_title()

        error_message = click_share_support.get_validation_error_empty_char()
        assert error_message == "Please specify a serial number"

    def test_get_warranty_with_less_than_minimize_chars(self, go_to_click_share_support_page):

        click_share_support = go_to_click_share_support_page
        click_share_support.input_serial_number(keys=test_serial_numbers['invalid']['less_than_minimize_chars'])
        click_share_support.click_get_info_button()
        click_share_support.wait_for_result_title()

        error_message = click_share_support.get_validation_error_min_chars_required()
        assert error_message == "Minimum 6 characters required"

    def test_get_warranty_with_wrong_format(self, go_to_click_share_support_page):

        click_share_support = go_to_click_share_support_page
        click_share_support.input_serial_number(keys=test_serial_numbers['invalid']['wrong_format'])
        click_share_support.click_get_info_button()
        click_share_support.wait_for_result_title()

        error_message = click_share_support.get_validation_error_wrong_format()
        assert error_message == "Please enter a valid serial number"

    def test_get_warranty_with_not_number(self, go_to_click_share_support_page):

        click_share_support = go_to_click_share_support_page
        click_share_support.input_serial_number(keys=test_serial_numbers['invalid']['not_number'])
        click_share_support.click_get_info_button()
        click_share_support.wait_for_result_title()

        error_message = click_share_support.get_validation_error_empty_char()
        assert error_message == "Please input number! (My suggestion)"
