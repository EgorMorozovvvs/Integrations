import json
import requests
from typing import List

from .Dataclasses import Item, RoutePoint
from .templates import *
from .interface import YandexDeliveryInterface

BASE_URL = 'https://b2b.taxi.tst.yandex.net/'
test_bearer = 'y2_AgAAAAD0Wcn4AAAPeAAAAAACJXtV-u9qs8IzQzWzJ0Cdt9pv-Wh1YS8'


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
        return requests.post(BASE_URL + url, headers=self.headers, data=json.dumps(current_data)).json()
