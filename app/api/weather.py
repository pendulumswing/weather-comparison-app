import os
from flask import request
from flask_restx import Resource
from . import api_rest
import requests


@api_rest.route('/weather')
class Weather(Resource):

    def post(self):
        OPENWEATHER_KEY = os.getenv('REACT_APP_OPENWEATHER_KEY')
        req = request.json
        value = req['value']
        url = f"http://api.openweathermap.org/data/2.5/weather?"\
                f"zip={value}&appid={OPENWEATHER_KEY}&units=metric"
        response = requests.get(url)
        return response.json()
