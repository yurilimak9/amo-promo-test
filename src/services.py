from src.entities import MockAirlinesInc
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


class SearchAvailableAirports:

    def __init__(self):
        self.__base_url = 'http://stub.2xt.com.br/air/airports'

    def execute(self) -> dict:
        config = dotenv_values('.env')
        api_key = config.get('API_KEY')
        url = f'{self.__base_url}/{api_key}'
        response = requests.get(url, auth=HTTPBasicAuth(config.get('USERNAME'), config.get('PASSWORD')))

        return loads(response.content)


class FlightRecommendationsService:

    def execute(self, going_data, return_data):
        going_mock_airlines_inc = MockAirlinesInc(**going_data)
        going_mock_airlines_inc.calculate_rates()

        return_mock_airlines_inc = MockAirlinesInc(**return_data)
        return_mock_airlines_inc.calculate_rates()

        options = []
        for option_ida in going_mock_airlines_inc.options:
            for option_volta in return_mock_airlines_inc.options:
                if option_volta.aircraft.model == option_ida.aircraft.model and option_volta.aircraft.manufacturer == option_ida.aircraft.manufacturer:
                    option = {
                        'aircraft': option_ida.aircraft.dict(),
                        'going': option_ida.dict(exclude={'aircraft'}),
                        'return': option_volta.dict(exclude={'aircraft'}),
                        'price': {
                            'fare': round(option_ida.price.fare + option_volta.price.fare, 2),
                            'fees': round(option_ida.price.fees + option_volta.price.fees, 2),
                            'total': round(option_ida.price.total + option_volta.price.total, 2)
                        }
                    }
                    options.append(option.copy())

        summary = {
            'going': going_mock_airlines_inc.summary.dict(),
            'return': return_mock_airlines_inc.summary.dict()
        }

        result = {
            'summary': summary.copy(),
            'options': options
        }

        return result
