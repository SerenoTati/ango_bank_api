
from abc import ABC, abstractmethod

from src.models.exchange_rate_model import ExchangeRateModel


class ScrapeService(ABC):
    """
    This is an abstract base class for a scrap service.
    """

    @abstractmethod
    def get_rates(self, url: str, cert_path:str='') -> list[ExchangeRateModel]:
        """
        Fetches content from the given URL and returns a list of ExchangeRateModel.
        """
        pass
