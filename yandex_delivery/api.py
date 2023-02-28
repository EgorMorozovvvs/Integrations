import json
import requests
from typing import List, Dict, Optional

from .Dataclasses import Item, RoutePoint
from .templates import *
from .interface import YandexDeliveryInterface

BASE_URL = 'https://b2b.taxi.tst.yandex.net/'
TEST_BASE_URL = 'https://b2b.taxi.tst.yandex.net/'
test_bearer = 'y2_AgAAAAD0Wcn4AAAPeAAAAAACJXtV-u9qs8IzQzWzJ0Cdt9pv-Wh1YS8'
platform_station_id = '4eb18cc4-329d-424d-a8a8-abfd8926463d'


class YandexDelivery(YandexDeliveryInterface):
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Accept-Language': 'ru',
            'Content-Type': 'application/json'
        }

    def check_price(self, items: List[Item],
                    route_points: List[RoutePoint],
                    cargo_options: List[str],
                    cargo_type: str,
                    taxi_class: str,
                    cargo_loaders: int = 0,
                    pro_courier: bool = False,
                    skip_door_to_door: bool = False
                    ) -> dict:
        current_data = check_price_template(**locals())
        url = 'b2b/cargo/integration/v2/check-price'
        return requests.post(TEST_BASE_URL + url, headers=self.headers, data=json.dumps(current_data)).json()

    def get_intervals_during_day(self, fullname: str, start_point: List[float]):
        current_data = get_intervals_during_day_template(**locals())
        url = 'b2b/cargo/integration/v2/delivery-methods'
        return requests.post(TEST_BASE_URL + url, headers=self.headers, data=json.dumps(current_data)).json()

    def get_tariffs(self, fullname: str, start_point: List[float]) -> dict:
        current_data = get_tariffs_template(**locals())
        url = 'b2b/cargo/integration/v2/tariffs'
        return requests.post(TEST_BASE_URL + url, headers=self.headers, data=json.dumps(current_data)).json()

    def get_identifier(self, location: str):
        url = 'api/b2b/platform/location/detect'
        current_data = {
            'location': location
        }
        return requests.post(TEST_BASE_URL + url, headers=self.headers, data=json.dumps(current_data)).json()

    def get_available_points_of_self_delivery(self,
                                              available_for_dropoff: bool = None,
                                              latitude: Dict[str, float] = None,
                                              longitude: Dict[str, float] = None,
                                              payment_method: str = None,
                                              payment_methods: List[str] = None,
                                              pickup_points_ids: List[str] = None,
                                              type: str = None) -> dict:
        current_data = get_available_points_of_self_delivery_template(**locals())
        url = 'api/b2b/platform/pickup-points/list'
        return requests.post(TEST_BASE_URL + url, headers=self.headers, data=json.dumps(current_data)).json()

    def pricing_calculator(self,
                           tariff: str,
                           total_weight: int,
                           source: Dict[str, str],
                           destination: Dict[str, str],
                           client_price: int = None,
                           payment_method: str = None,
                           total_assessed_price: int = None,
                           ) -> dict:
        current_data = pricing_calculator_template(**locals())
        url = 'api/b2b/platform/pricing-calculator'
        return requests.post(TEST_BASE_URL + url, headers=self.headers, data=json.dumps(current_data)).json()

    def get_intervals(self,
                      station_id: str,
                      full_address: str = None,
                      geo_id: int = None,
                      self_pickup_id: str = None,
                      send_unix: bool = None,
                      last_mile_policy: str = 'time_interval') -> dict:
        url = f'api/b2b/platform/offers/info?station_id={station_id}'
        for key, value in locals().items():
            if value is not None:
                url += f'&{key}={value}'
        # TODO error 'debug_message': '/handlers.api.b2b.platform.offers.info.multiple station_id are specified'
        return requests.get(TEST_BASE_URL + url, headers=self.headers).json()

    def find_full_address(self, term: str) -> dict:
        url = f'/location?term={term}'
        return requests.get(TEST_BASE_URL + url, headers=self.headers).json()

