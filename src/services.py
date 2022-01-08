from json import loads
from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth
import requests


class SearchFlightOptions:

    def __init__(self):
        self.__base_url = 'http://stub.2xt.com.br/air/search'

    def execute(self, departure_airport: str, arrival_airport: str, departure_date: str):
        config = dotenv_values('.env')
        api_key = config.get('API_KEY')
        url = f'{self.__base_url}/{api_key}/{departure_airport}/{arrival_airport}/{departure_date}'
        response = requests.get(url, auth=HTTPBasicAuth(config.get('USERNAME'), config.get('PASSWORD')))

        return response
