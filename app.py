from flask import Flask, Response
from src.services import SearchAvailableAirports, SearchFlightOptions
from src.entities import MockAirlinesInc
from datetime import datetime
from json import dumps

app = Flask(__name__)
app.config['FLASK_APP'] = 'app'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


@app.route('/api/search/<string:iata_origin>/<string:iata_destiny>/<string:departure_date>/<string:return_date>')
def index(iata_origin, iata_destiny, departure_date, return_date):
    iata_origin = iata_origin.upper()
    iata_destiny = iata_destiny.upper()

    if iata_origin == iata_destiny:
        message = dumps({'message': 'Os aeroportos de origem e destino não podem ser iguais'})
        return Response(message, status=400, mimetype='application/json')

    search_available_airports = SearchAvailableAirports()
    airports = search_available_airports.execute()
    if airports.get(iata_origin) is None or airports.get(iata_destiny) is None:
        message = dumps({'message': 'O aeroporto informado não foi encotrado na nossa base'})
        return Response(message, status=400, mimetype='application/json')

    departure_date = datetime.strptime(departure_date, '%Y-%m-%d')
    return_date = datetime.strptime(return_date, '%Y-%m-%d')
    if departure_date >= return_date:
        message = dumps({'message': 'A data de retorno não pode ser menor ou igual à data de partida'})
        return Response(message, status=400, mimetype='application/json')

    search_flight_options = SearchFlightOptions()
    data = search_flight_options.execute(iata_origin, iata_destiny, str(departure_date.date()))

    mock_airlines_inc = MockAirlinesInc(**data.json())
    for flight in mock_airlines_inc.options:
        flight.price.calculate_fee()
        flight.price.calculate_total()

        flight.meta.calculate_range(mock_airlines_inc.summary.from_.lat, mock_airlines_inc.summary.from_.lon, mock_airlines_inc.summary.to.lat, mock_airlines_inc.summary.to.lon)

    return Response(mock_airlines_inc.json(), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
