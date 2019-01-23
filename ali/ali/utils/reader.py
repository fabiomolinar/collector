"""
Class of objects that know how to read specific data
"""
import warnings
import re

from collections import deque

class PriceReader():
    """
    An object that, given a string, can take monetary values out of it.

    This object should have only one method exposed to the user: read().
        If this method returns TRUE, it means we could read the data.
    And the user should be able to get four properties: preffered_currency, amount, currency, is_average
    The property is_average let's us know if the amount calculated is a single value or if it was 
    calculated by averaging other numbers.
    """
    from . import currencies
    
    common_currencies = currencies.common_currencies
    other_currencies = currencies.other_currencies
    space_newline_pattern = re.compile(r"\s|\n")
    digit_pattern = re.compile(r"\d")
    default_value = ""

    def __init__(self, preffered_currency=None):
        if preffered_currency:
            self.preffered_currency = preffered_currency
        else:
            self._preffered_currency = preffered_currency
        self._amount = None
        self._currency = None
        self._is_average = None

    @property
    def _is_average(self):
        if not self._is_average:
            warnings.warn("The property is_average is not set. Try running PriceReader.read() first.")
        return self._amount

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
        raise ValueError("Currency code don't exist on list of currencies")
    
    def currency_exists(self, currency):
        """Checks if a certain currency CODE exists on our list of currencies"""
        for c in self.__class__.common_currencies + self.__class__.other_currencies:
            if currency == c["code"]:
                return True
        return False

    def read(self, *args, currency=None, amount=None):
        """
        Tries to read information about the amount and currency from a given string
        The user can specify which strings contain the amount information and the 
        currency information. Otherwise, it will be considered that this information is contained 
        as a list of strings passed to args.

        This method returns TRUE if it can parse the data succesfully (both amount and currency).
        It returns FALSE otherwise.
        """
        if not currency:
            currency = self.__class__.default_value
        if not amount:
            amount = self.__class__.default_value
        return self.extract_amount(*args, amount=amount) and self.extract_currency(*args, currency=currency)

    def extract_amount(self, *args, amount):
        if type(amount) != str:
            raise TypeError("A string is expected.")
        amount = self.__class__.clean_string(*args, var=amount)
        # TO FINISH
        
    
    def extract_currency(self, *args, currency):
        if type(currency) != str:
            raise TypeError("A string is expected.")
        currency = self.__class__.clean_string(*args, var=currency)
        first_digit_position = self.__class__.get_first_digit_position(currency)
        last_digit_position = self.__class__.get_last_digit_position(currency)
        currency_code = self.search_currency(currency[0:first_digit_position])
        if not currency_code:
            currency_code = self.search_currency(currency[last_digit_position:])
        if not currency_code:
            return False
        self._currency = currency_code
        return True
        

    def search_currency(self, var):
        found_currencies = []
        for c in self.__class__.common_currencies + self.__class__.other_currencies:
            if var in c["code"]:
                return c["code"]
            for s in c["aka"]:
                if var.upper() in s.upper():
                    if c["code"] == self.preffered_currency or not self.preffered_currency:
                        return c["code"]
                    found_currencies.append(c["code"])
        if len(found_currencies) > 0:
            return found_currencies[0]
        return None

    @classmethod
    def get_first_digit_position(cls, var):
        first = next(cls.digit_pattern.finditer(var))
        return first.start()

    @classmethod
    def get_last_digit_position(cls, var):
        last = deque(cls.digit_pattern.finditer(var)).pop()
        return last.end()
        
    @classmethod
    def clean_string(cls, *args, var):
        if var == cls.default_value and len(args) > 0:
            var = "".join(args)
        var = re.sub(cls.space_newline_pattern,"",var)
        return var
