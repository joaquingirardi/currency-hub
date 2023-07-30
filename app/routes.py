from flask import Blueprint, Flask, request
from .utils import get_dollar_conversion, get_dollar_conversion_by_date
import os

bp = Blueprint('api', __name__)
usd_api_url = os.environ.get('USD_API_PATH')
historical_usd_api_url = os.environ.get('HISTORICAL_USD_API_PATH')

@bp.route('/')
def index():
    return "Hello, World!"


@bp.route('/dollar')
def dollar():
    return get_dollar_conversion(usd_api_url)


@bp.route('/dollar-date')
def dollar_by_date():
    date = request.args.get('date') or None
    source = request.args.get('source') or None
    return get_dollar_conversion_by_date(historical_usd_api_url, date, source)
