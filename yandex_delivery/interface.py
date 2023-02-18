from abc import ABC
from typing import List, Dict, Optional
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

    def get_available_points_of_self_delivery(self,
                                              available_for_dropoff: bool = False,
                                              latitude: Optional[Dict[str, float]] = None,
                                              longitude: Optional[Dict[str, float]] = None,
                                              payment_method: Optional[str] = None,
                                              payment_methods: Optional[List[str]] = None,
                                              pickup_points_ids: Optional[List[str]] = None,
                                              type: Optional[str] = None) -> dict:
        """Получение списка точек самопривоза и самостоятельного получения заказа.
        Запрос для получения списка точек самопривоза и самостоятельного получения заказа.
        Может быть пустым, в этом случае вернутся все доступные точки.

        available_for_dropoff: Возможность отгрузки заказов в точку (самопривоз).
        latitude: {'from': float, 'to': float} - широта
        longitude: {'from': float, 'to': float} - долгота
        payment_method:
            1:'already_paid'
            2:'cash_on_receipt'
            3:'card_on_receipt'
            4:'cashless'
        payment_methods: Набор типов оплаты, которые должны быть доступны в точке самостоятельного получения заказа.
        pickup_point_ids: Идентификаторы точек получения заказа.
        type:
            1:"pickup_point"
            2:"terminal"
            3:"post_office"
            4:"sorting_center"

            pickup_point - пункт выдачи заказов; terminal - постомат; post_office - почтовое отделение; sorting_center - сортировочный центр;
        """
        raise NotImplementedError

    def preliminary_orders_assessment(self,
                                      tariff: str,
                                      total_weight: int,
                                      source: Dict[str, str],
                                      destination: Dict[str, str],
                                      client_price: Optional[int] = None,
                                      payment_method: Optional[str] = None,
                                      total_assessed_price: Optional[int] = None,
                                      ) -> dict:
        """Расчет стоимости доставки на основании переданных параметров заказа.

        POST b2b-authproxy.taxi.yandex.net/api/b2b/platform/pricing-calculator

        tariff: Тариф доставки. Нужно выбрать 1 из 2.
        1) time_interval - доставка до двери в интервал;
        2) self_pickup - доствка до ПВЗ;

        source: В данном объекте 2 параметра. Необходимо заполнить 1 из 2.
                {
                    'address': Адрес точки отправки,
                    'platform_statioin_id: Id склада отправки, зарегистрированного в платформе.
                }
        destination: В данном объекте 2 параметра. Необходимо заполнить 1 из 2.
                {
                    'address': Адрес точки получения,
                    'platform_statioin_id: Id ПВЗ или постамата, зарегистрированного в платформе, в который нужна доставка.
                }

        client_price: Cумма к оплате с получателя в копейках.

        payment_method: Нужно ввести 1, 2 или 3
        default - already_paid
        Cпособ оплаты товаров.
        1) already_paid - уже оплачено;
        2) card_on_receipt - оплата картой при получении;
        3) cash_on_receipt - оплата наличными при получении;

        total_assessed_price: Суммарная оценочная стоимость посылок в копейках.

        total_weight: Cуммарный вес посылки в граммах."""
        raise NotImplementedError
