
from typing import override

from src.models.exchange_rate_model import ExchangeRateModel
from src.services.scrape_service import ScrapeService


class ExchangeRateRepository:
    """
    This class is responsible for managing exchange rates.
    It provides methods to fetch and parse exchange rate data from a given URL.
    """

    def __init__(self, scrap_service: ScrapeService):
        self.scrap_service = scrap_service
    @override
    def get_rates(self, url: str, cert_path:str='') -> list[ExchangeRateModel]:
        """
        Fetches and parses exchange rates from the given URL.
        """
        return self.scrap_service.get_rates(url, cert_path)
