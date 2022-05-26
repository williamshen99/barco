from testdata.test_serial_numbers import test_serial_numbers


class TestClickShareSupportWarranty:

    def test_get_warranty_normally(self, go_to_click_share_support_page):

        setup = go_to_click_share_support_page
        setup.click_share_support.input_serial_number()
        setup.click_share_support.click_get_info_button()
        setup.click_share_support.wait_for_result_title()
        setup.click_share_support.wait_for_result_detail()

        result_detail = setup.click_share_support.get_result_detail()
        result_detail_list = result_detail.split('\n')

        for idx in range(0, len(result_detail_list) - 1, 2):
            result_item = result_detail_list[idx]
            result_value = result_detail_list[idx+1]

            if result_item not in test_serial_numbers['valid']['with_warranty'].keys():
                raise ValueError(f'unexpected response attribute: {result_item}')
            assert test_serial_numbers['valid']['with_warranty'][result_item] == result_value

    def test_get_warranty_with_no_warranty_number(self, go_to_click_share_support_page):

        setup = go_to_click_share_support_page
        setup.click_share_support.input_serial_number(keys=test_serial_numbers['invalid']['no_warranty'])
        setup.click_share_support.click_get_info_button()
        setup.click_share_support.wait_for_result_title()
        setup.click_share_support.wait_for_result_detail()

        result_detail = setup.click_share_support.get_result_detail()


#TODO: error handling