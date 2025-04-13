import json

class ExchangeRateModel:
    """
    This class represents an exchange rate model.
    """
    #


    def __init__(self, currency: dict, buy_rate: str, sell_rate: str):
        """
        Initializes the ExchangeRateModel with currency name, buy rate, and sell rate.
        """
        self.currency = currency
        self.buy_rate = buy_rate
        self.sell_rate = sell_rate
        

    def to_dict(self):
        """
        Converts the ExchangeRateModel instance to a dictionary.
        """
        return {
            'currency': self.currency,
            'buy_rate': self.buy_rate,
            'sell_rate': self.sell_rate
        }
    @classmethod
    def from_dict(cls, data):
        """
        Creates an ExchangeRateModel instance from a dictionary.
        """
        return cls(
            currency = data['currency'],
            buy_rate=data['buy_rate'],
            sell_rate=data['sell_rate']
        )

    def to_json(self):
        """
        Converts the ExchangeRateModel instance to a JSON string.
        """
     
        return json.dumps(self.to_dict())
  