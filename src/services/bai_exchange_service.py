from typing import override

import requests
from bs4 import BeautifulSoup

from src.models.exchange_rate_model import ExchangeRateModel
from src.services.scrap_service import ScrapeService


class BAIExchangeService(ScrapeService):

    """
    This class implements the scrap_service interface for scraping data from Bai.
    """
    def __init__(self):
    @classmethod
    def fetch_content(cls, url: str):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    @classmethod
    def parse_rates(cls, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        rates_table = soup.find('table', class_='table-striped')
        rows = rates_table.find('tbody').find_all('tr')

        exchange_rates = []
        for row in rows:

            cells = row.find_all('td')
            currency = cells[0].find('div,', class_='exchange_rates-list--coin-info--value').text.strip()
            sell_rate = cells[1].text.strip()
            buy_rate = cells[2].text.strip()

            exchange_rates.append({
                'currency': currency,
                'sell_rate': sell_rate,
                'buy_rate': buy_rate
            })
        return exchange_rates
 
    @override
    def get_rates(self, url: str)-> list[ExchangeRateModel]:
        """
        Fetches and parses exchange rates from the given URL.
        """
        html_content = self.fetch_content(url)
        if not html_content:
            raise Exception("No content fetched from the URL.")
        parsed_rates = self.parse_rates(html_content)

        if not parsed_rates:
            raise Exception("No exchange rates found in the fetched content.")
        exchange_rate_list = []
        for rate in parsed_rates:
            exchange_rate_list.append(ExchangeRateModel.from_dict(rate))

        if not exchange_rate_list:
            raise Exception("No exchange rates found in the parsed content.")

        return exchange_rate_list
        