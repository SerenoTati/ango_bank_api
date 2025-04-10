
class ExchangeRateModel:
    def __init__(self, currency: str, buy_rate: float, sell_rate: float):
        """
        Initializes the ExchangeRateModel with currency name, buy rate, and sell rate.
        """
        self.currency = currency
        self.buy_rate = buy_rate
        self.sell_rate = sell_rate
        
    @classmethod
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
            currency=data['currency'],
            buy_rate=float(data['buy_rate']),
            sell_rate=float(data['sell_rate'])
        )
    @classmethod
    def to_json(self):
        """
        Converts the ExchangeRateModel instance to a JSON string.
        """
        import json
        return json.dumps(self.to_dict())
  