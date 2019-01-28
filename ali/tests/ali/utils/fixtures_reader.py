price_reader_cases = [
    # string 'dq' don't match with any existing currency
    # test for different currency positions and presence or not of spaces
    {"to_test": "SLL 41.00", "preffered_currency": "", "expected_currency": "SLL","expected_amount": 41.0},
    {"to_test": "SLL41.00", "preffered_currency": "", "expected_currency": "SLL","expected_amount": 41.0},
    {"to_test": "41.00 SLL", "preffered_currency": "", "expected_currency": "SLL","expected_amount": 41.0},
    {"to_test": "41.00SLL", "preffered_currency": "", "expected_currency": "SLL","expected_amount": 41.0},
    # test for gibberish on data string
    {"to_test": "SLL dq 41.00", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 41.0},
    {"to_test": "SLLdq41.00", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 41.0},
    {"to_test": "SLL 41.00 dq", "preffered_currency": "", "expected_currency": "SLL","expected_amount": 41.0},
    {"to_test": "41.00dqSLL", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 41.0},
    {"to_test": "SLL dq 1000.00 - 2000.00", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1500.0},
    {"to_test": "SLL 1000.00 dq - 2000.00", "preffered_currency": "", "expected_currency": "SLL","expected_amount": 1500.0},
    {"to_test": "SLL 1000.00 - 2000.00 dq", "preffered_currency": "", "expected_currency": "SLL","expected_amount": 1500.0},
    {"to_test": "SLLdq 1000.00 - 2000.00", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1500.0},
    {"to_test": "dqSLL 1000.00 - 2000.00", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1500.0},
    # test for preffered currency setting
    {"to_test": "$ 1000.00 - 2000.00", "preffered_currency": "USD", "expected_currency": "USD","expected_amount": 1500.0},
    {"to_test": "$ 1000.00 - 2000.00", "preffered_currency": "ARS", "expected_currency": "ARS","expected_amount": 1500.0},
    {"to_test": "$ 1000.00 - 2000.00", "preffered_currency": "SGD", "expected_currency": "SGD","expected_amount": 1500.0},
    # test for different decimal and thousands separators
    {"to_test": "SLL dq 1,000.00 - 2,000.00", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1500.0},
    {"to_test": "SLL 1 000.00 dq - 2 000.00", "preffered_currency": "", "expected_currency": "SLL","expected_amount": 1500.0},
    {"to_test": "SLL 1 000,00 dq - 2 000,00", "preffered_currency": "", "expected_currency": "SLL","expected_amount": 1500.0},
    {"to_test": "SLL 1.000,00 - 2.000,00 dq", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1500.0},
    {"to_test": "SLL dq 1,120.10", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1120.1},
    {"to_test": "SLL 1 030.2 dq", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1030.2},
    {"to_test": "SLL 1 410,30 dq", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1410.3},
    {"to_test": "SLL 1.320,04", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1320.04},
    # testing 'currency' and 'amount' inputs
    {"to_test": "SLL 1.320,04", "currency":"SLL", "amount":"dq 1320.04", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1320.04},
    {"to_test": "SLL 1.320,04", "currency":"SLL dq", "amount":"1320.04 dq", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1320.04},
    {"to_test": "SLL 1.320,04", "currency":"dqSLL", "amount":"1,320.04 dq", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1320.04},
    {"to_test": "SLL 1.320,04", "currency":"SLL-dq", "amount":"dq 1 320.04", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1320.04},
    {"to_test": "SLL 1000.00 - 2000.0", "currency":" SLL ", "amount":"1000.00 - 2000.0", "preffered_currency": "SLL", "expected_currency": "SLL","expected_amount": 1500.0},
]