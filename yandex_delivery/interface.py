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

    def get_intervals_during_day(self, fullname: str, start_point: List[float]) -> dict:
        """В ответе возвращается список услуг, доступных в точке, с учетом их опций.
            Ответ состоит из двух объектов:

            express_delivery — содержит доступные тарифы и опции для "Экспресс-доставки"
            same_day_delivery — содержит доступные интервалы для доставки "В течение дня"
            Каждый из объектов содержит поле allowed, которое обозначает доступность данного режима доставки."""
        raise NotImplementedError

    def get_tariffs(self, fullname: str, start_point: List[float]) -> dict:
        """Получение тарифов, доступных в точке
            В ответе в поле supported_requirements возвращаются возможные дополнительные требования."""
        raise NotImplementedError

    def search_ways_of_delivery(self,
                                sender_id: int) -> dict:
        """Запрос позволяет получить список вариантов доставки по заданным габаритам заказа и адресу получателя."""
        raise NotImplementedError

    def find_full_address(self, term: str) -> dict:
        """Запрос позволяет получить идентификатор населенного пункта и составляющие адреса
        (страну, область, населенный пункт и район) по заданной строке."""
        raise NotImplementedError

    def get_offer_intervals(self, station_id: str) -> dict:
        """Получение расписания вывозов в регионы. В качестве конечного пункта нужно указать либо geo_id (геоайди конечного региона),
        либо full_address (строковый конечный адрес), либо self_pickup_id (id пвз)"""
        raise NotImplementedError

    def get_identifier(self, location: str) -> dict:
        """Получение идентификатора населённого пункта (geo_id) по адресу или его фрагменту."""
        raise NotImplementedError

    def get_available_points_of_self_delivery(self) -> dict:
        """Получение списка точек самопривоза и самостоятельного получения заказа."""
        raise NotImplementedError