class CurrencyModel:
    """
    This class represents a currency model with attributes for currency name, buy rate, and sell rate.
    """
    
    def __init__(self, currency: str, buy_rate: float, sell_rate: float):
        self.currency = currency
        self.buy_rate = buy_rate
        self.sell_rate = sell_rate

    def __repr__(self):
        return f"CurrencyModel(currency={self.currency}, buy_rate={self.buy_rate}, sell_rate={self.sell_rate})"
    def __str__(self):
        return f"Currency: {self.currency}, Buy Rate: {self.buy_rate}, Sell Rate: {self.sell_rate}"
    def to_dict(self):
        """
        Converts the currency model to a dictionary.
        """
        return {
            'currency': self.currency,
            'buy_rate': self.buy_rate,
            'sell_rate': self.sell_rate
        }
    @classmethod
    def from_dict(cls, data):
        """
        Creates a currency model instance from a dictionary.
        """
        return cls(
            currency=data['currency'],
            buy_rate=float(data['buy_rate']),
            sell_rate=float(data['sell_rate'])
        )
