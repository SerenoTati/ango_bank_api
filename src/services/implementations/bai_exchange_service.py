from typing import override

import requests
from bs4 import BeautifulSoup

from src.models.exchange_rate_model import ExchangeRateModel
from src.services.scrape_service import ScrapeService


class BAIExchangeService(ScrapeService):

    """
    This class implements the scrap_service interface for scraping data from Bai.
    """
    def __init__(self):
        pass

    @classmethod
    def fetch_content(cls, url: str, cert_path: str = ''):
        
        if cert_path is not None:
          
            response = requests.get(url, verify=False) 
         
        else:
            
            response = requests.get(url)

        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    @classmethod
    def parse_rates(cls, html_content):
        print(html_content)
        soup = BeautifulSoup(html_content, 'html.parser')
        rates_table = soup.find('table', class_='table-striped')

        if rates_table is None:
            print("Warning: No table with class 'table-striped' found.")
            return []  # Return an empty list if the table is not found

        tbody = rates_table.find('tbody')
        if tbody is None:
            print("Warning: No tbody found in the table.")
            return []  # Return an empty list if the tbody is not found

        rows = tbody.find_all('tr')
        exchange_rates = []

        for row in rows:
            cells = row.find_all('td')
            if len(cells) < 3:
                print(f'Warning: Row has less than 3 cells. Skipping row: {row}')
                continue  # Skip this row if it doesn't have enough cells

            currency_div = cells[0].find('div', class_='exchange-rates-list--coin-info') #.find('div', class_='exchange-rates-list--coin-info-value')
            if currency_div is None:
                print(f"Warning: No currency div found in row. Skipping row: {row}")
                continue  # Skip this row if the currency div is not found

            currency_name = currency_div.find('div', class_='exchange-rates-list--coin-info--name').text.strip()
            currency_symbol = currency_div.find('div', class_='exchange-rates-list--coin-info--value').text.strip()
            sell_rate = cells[1].text.strip()
            buy_rate = cells[2].text.strip()

            exchange_rates.append({
                'currency': {'name': currency_name, 'symbol': currency_symbol},
                'sell_rate': sell_rate,
                'buy_rate': buy_rate
            })

        return exchange_rates
    @override
    def get_rates(self, url: str, cert_path:str='')-> list[ExchangeRateModel]:
        """
        Fetches and parses exchange rates from the given URL.
        """
        html_content = self.fetch_content(url, cert_path)
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
