from pydantic import BaseModel, Field
from typing import List


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


class Aircraft(BaseModel):
    model: str
    manufacturer: str


class Meta(BaseModel):
    range: float
    cruise_speed_kmh: float
    cost_per_km: float


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

