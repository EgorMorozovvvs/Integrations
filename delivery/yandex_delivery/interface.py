from abc import ABC
from typing import List, Dict
from .Dataclasses import Item, RoutePoint


class YandexDeliveryInterface(ABC):
    def create_order(self, callback_url: str = str(), assign_robot: bool = False, ):
        """Создание заявки"""
        raise NotImplementedError()

    def check_price(self, items: List[Item],
                    route_points: List[RoutePoint],
                    cargo_options: List[str],
                    cargo_type: str,
                    taxi_class: str,
                    cargo_loaders: int = 0,
                    pro_courier: bool = False,
                    skip_door_to_door: bool = False
                    ) -> dict:
        """Первичная оценка стоимости без создания заявки"""
        raise NotImplementedError()
