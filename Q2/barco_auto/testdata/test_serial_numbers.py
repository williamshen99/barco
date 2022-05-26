
test_serial_numbers = {
    'valid':
        {
            'with_warranty':
                {
                    'serial_number': '1863552437',
                    'Description': 'CLICKSHARE CX-50 SET NA',
                    'Part number': 'R9861522NA',
                    'Delivery date': '05/07/2020 00:00:00',
                    'Installation date': '09/28/2020 09:16:22',
                    'Warranty end date': '09/27/2021 09:16:22',
                    'Service contract end date': '01/01/0001 00:00:00'
                }
        },

    'invalid':
        {
            'no_warranty': '186232437',
            'empty_char': '',
            'less_than_minimize_chars': '12345',
            'not_number': 'abcdef'
        }
}
