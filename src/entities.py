from pydantic import BaseModel, Field
from typing import List
from .utils import haversine
from datetime import datetime


class Airport(BaseModel):
    iata: str
    city: str
    lat: float
    lon: float
    state: str


class Summary(BaseModel):
    departure_date: str
    from_: Airport = Field(None, alias='from')
    to: Airport
    currency: str


class Price(BaseModel):
    fare: float
    fees: float
    total: float

    def calculate_fee(self):
        result = self.fare * 0.1
        self.fees = round(result, 2) if result > 40 else 40
        return self

    def calculate_total(self):
        result = self.fare + self.fees
        self.total = round(result, 2)
        return self


class Aircraft(BaseModel):
    model: str
    manufacturer: str


class Meta(BaseModel):
    range: float
    cruise_speed_kmh: float
    cost_per_km: float

    def calculate_range(self, lat1: float, long1: float, lat2: float, long2: float):
        result = haversine(lat1, long1, lat2, long2)
        self.range = round(result, 2)
        return self

    def calculate_cruise_speed_kmh(self, departure_time: str, arrival_time: str):
        departure_time = datetime.strptime(departure_time, '%Y-%m-%dT%H:%M:%S')
        arrival_time = datetime.strptime(arrival_time, '%Y-%m-%dT%H:%M:%S')

        time_in_seconds = (arrival_time - departure_time).seconds
        time = time_in_seconds / 3600

        result = self.range / time
        self.cruise_speed_kmh = round(result, 2)
        return self

    def calculate_cost_per_km(self, fare):
        result = fare / self.range
        self.cost_per_km = round(result, 2)
        return self


class Flight(BaseModel):
    departure_time: str
    arrival_time: str
    departure_time: str
    price: Price
    aircraft: Aircraft
    meta: Meta


class MockAirlinesInc(BaseModel):
    summary: Summary
    options: List[Flight]
