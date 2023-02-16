import json
import requests
from typing import List

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

    def search_ways_of_delivery(self,
                                sender_id: int) -> dict:
        ...

    def find_full_address(self, term: str): # BAD
        url = f'/location?term={term}'
        return requests.get(BASE_URL + url, headers=self.headers).json()

    def get_identifier(self, location: str):
        url = '/api/b2b/platform/location/detect'
        current_data = {
            'location': location
        }
        return requests.post(TEST_BASE_URL + url, headers=self.headers, data=json.dumps(current_data)).json()

    def get_available_points_of_self_delivery(self) -> dict:
        url = '/api/b2b/platform/pickup-points/list'
        return requests.post(TEST_BASE_URL + url, headers=self.headers).json()



# TODO разобраться с start_point