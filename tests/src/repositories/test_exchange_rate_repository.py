from unittest.mock import  Mock
from src.repository.exchance_rate_repository import ExchangeRateRepository
from src.services.scrape_service import ScrapeService

mocked_rates = [
    {
        "currency": "AED",
        "currency_name": "Dirham Emirados Arabes",
        "sell_rate": "260.41610",
        "buy_rate": "255.30990"
    },
    {
        "currency": "CAD",
        "currency_name": "Dolar Canadiano",
        "sell_rate": "675.12993",
        "buy_rate": "661.89209"
    },
    {
        "currency": "CHF",
        "currency_name": "Franco Suíço",
        "sell_rate": "1120.49650",
        "buy_rate": "1098.52598"
    }
]

def test_get_rates():
 
   mock_scrape_service =  Mock(spec=ScrapeService)

   mock_scrape_service.get_rates.return_value = mocked_rates
   url = "https://www.example.com/rates"
   cert_path = 'assets/certificates/www.bancobai.ao.pem'
   request = ExchangeRateRepository(mock_scrape_service).get_rates(url,)

   assert request[0]["currency"] == "AED"
   assert request[0]["currency_name"] == "Dirham Emirados Arabes"
   assert request[0]["sell_rate"] == "260.41610"
   assert request[0]["buy_rate"] == "255.30990"
   

