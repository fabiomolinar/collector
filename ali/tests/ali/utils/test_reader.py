import unittest
from ali.utils import reader

class TestPriceReaderClass(unittest.TestCase):
    def setUp(self):
        self.pr = reader.PriceReader()
        from tests.ali.utils.fixtures_reader import price_reader_cases as cases
        self.cases = cases
    
    def test_currency(self):
        for c in self.cases:
            with self.subTest(c=c["to_test"]):
                if "preffered_currency" in c:
                    if c["preffered_currency"] != "":
                        self.pr.preffered_currency = c["preffered_currency"]
                self.pr.read(c["to_test"])
                self.assertEqual(self.pr.currency,c["expected_currency"])

    def test_amount(self):
        for c in self.cases:
            with self.subTest(c=c["to_test"]):
                self.pr.read(c["to_test"])
                self.assertEqual(self.pr.amount,c["expected_amount"])

    def test_currency_input(self):
        for c in self.cases:
            with self.subTest(c=c):
                if "currency" not in c:
                    self.skipTest("no currency input")
                if "preffered_currency" in c:
                    if c["preffered_currency"] != "":
                        self.pr.preffered_currency = c["preffered_currency"]
                self.pr.read(c["to_test"], currency=c["currency"])
                self.assertEqual(self.pr.currency,c["expected_currency"])

    def test_amount_input(self):
        for c in self.cases:
            with self.subTest(c=c):
                if "amount" not in c:
                    self.skipTest("no amount input")
                self.pr.read(c["to_test"], amount=c["amount"])
                self.assertEqual(self.pr.amount,c["expected_amount"])

    def test_amount_and_currency_input(self):
        for c in self.cases:
            with self.subTest(c=c):
                if "amount" not in c and "currency" not in c:
                    self.skipTest("no amount nor currency input")
                self.pr.read(currency=c["currency"], amount=c["amount"])
                self.assertEqual(self.pr.amount,c["expected_amount"])        

    def test_preffered_currency(self):
        for c in self.cases:
            with self.subTest(c="to test: \"" + c["to_test"] + "\" with preffered currency as " + c["preffered_currency"]):
                if "preffered_currency" not in c:
                    self.skipTest("no preffered currency set on test data")
                if c["preffered_currency"] == "":
                    self.skipTest("no preffered currency set on test data")
                self.pr.preffered_currency = c["preffered_currency"]
                self.pr.read(c["to_test"])
                self.assertEqual(self.pr.currency,c["expected_currency"])

if __name__ == '__main__':
    unittest.main()
