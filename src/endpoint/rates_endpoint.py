from flask import Blueprint, jsonify

from src.repository.exchance_rate_repository import ExchangeRateRepository
from src.services.implementations.bai_exchange_service import BAIExchangeService

rate_endpoint_blueprint = Blueprint('rate_endpoint_blueprint', __name__, url_prefix='/api/v1/rates')



@rate_endpoint_blueprint.route('/bai', methods=['GET'])
def get_bai_rates():
    bai_repository = ExchangeRateRepository(BAIExchangeService())
    """
    Endpoint to get exchange rates from Bai.
    """
    try:
        
        rates =bai_repository.get_rates('https://www.bancobai.ao/pt/cambios-e-valores', cert_path='/assets/certificates/www.bancobai.ao.pem')
        if not rates:
            return jsonify({"error": "No exchange rates found."}), 404

        bai_rates = [rate.to_dict() for rate in rates]
        return jsonify({'bai':bai_rates})
    
    except Exception as e:
        return {"error": str(e)}, 500
    
@rate_endpoint_blueprint.route('/all', methods=['GET'])
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