"""
Class of objects that know how to read specific data
"""
import warnings

class PriceReader():
    """
    An object that, given a string, can take monetary values out of it.

    This object should have only one method exposed to the user: read().
    And the user should be able to get three properties: preffered_currency, amount, currency
    """
    from . import currencies
    
    common_currencies = currencies.common_currencies
    other_currencies = currencies.other_currencies

    def __init__(self, preffered_currency = "USD"):
        self.preffered_currency = preffered_currency
        self._amount = None
        self._currency = None

    @property
    def amount(self):
        if not self._amount:
            warnings.warn("The property amount is not set. Try running PriceReader.read() first.")
        return self._amount
    
    @property
    def currency(self):
        if not self._currency:
            warnings.warn("The property currency is not set. Try running PriceReader.read() first.")
        return self._currency

    @property
    def preffered_currency(self):
        return self._preffered_currency

    @preffered_currency.setter
    def preffered_currency(self, preffered_currency):
        if self.currency_exists(preffered_currency):
            self._preffered_currency = preffered_currency
        raise TypeError("Currency code don't exist on list of currencies")
    
    def currency_exists(self, currency):
        for c in PriceReader.common_currencies + PriceReader.other_currencies:
            if currency == c["code"]:
                return True
        return False

    def read(self, *args, currency="", amount=""):
        self.extract_amount(*args, amount=amount)
        self.extract_currency(*args, currency=currency)

    def extract_amount(self, *args, amount=""):
        if type(amount) != str:
            raise TypeError("A string is expected.")
        
    
    def extract_currency(self, *args, currency=""):
        if type(currency) != str:
            raise TypeError("A string is expected.")
