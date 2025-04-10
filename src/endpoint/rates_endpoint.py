from flask import Flask, jsonify

from src.repository.exchance_rate_repository import ExchangeRateRepository
from src.services.bai_exchange_service import BAIExchangeService

app = Flask(__name__)



@app.route('api/v1/rates/bai', methods=['GET'])
def get_bai_rates():
    bai_repository = ExchangeRateRepository(BAIExchangeService())
    """
    Endpoint to get exchange rates from Bai.
    """
    try:
        
        bai_rates =bai_repository.get_rates('https://bai.com/exchange-rates')
        return jsonify(bai_rates), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('api/v1/rates/all', methods=['GET'])
def get_all_rates():
    """
    Endpoint to get exchange rates from all sources.
    """
    try:
        # Assuming you have a function or class to fetch rates from all sources
        # rates = get_all_exchange_rates()
        return jsonify({
                "bai": get_bai_rates(),
    })
    except Exception as e:
        return jsonify({"error": str(e)}), 500