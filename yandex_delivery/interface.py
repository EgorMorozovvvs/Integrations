from abc import ABC
from typing import List, Dict, Union
from .Dataclasses import Item, RoutePoint


class YandexDeliveryInterface(ABC):
    def create_order(self, ...):
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
        """Первичная оценка стоимости без создания заявки

        b2b/cargo/integration/v2/check-price"""
        raise NotImplementedError()

    def get_intervals_during_day(self, fullname: str, start_point: List[float]) -> dict:
        """В ответе возвращается список услуг, доступных в точке, с учетом их опций.

            b2b/cargo/integration/v2/delivery-methods

            Ответ состоит из двух объектов:

            express_delivery — содержит доступные тарифы и опции для "Экспресс-доставки"
            same_day_delivery — содержит доступные интервалы для доставки "В течение дня"
            Каждый из объектов содержит поле allowed, которое обозначает доступность данного режима доставки."""
        raise NotImplementedError()

    def get_tariffs(self, fullname: str, start_point: List[float]) -> dict:
        """Получение тарифов, доступных в точке

        b2b/cargo/integration/v2/tariffs

        В ответе в поле supported_requirements возвращаются возможные дополнительные требования."""
        raise NotImplementedError()

    def search_ways_of_delivery(self,
                                sender_id: int) -> dict:
        """Запрос позволяет получить список вариантов доставки по заданным габаритам заказа и адресу получателя."""
        raise NotImplementedError()

    def find_full_address(self, term: str) -> dict:
        """Запрос позволяет получить идентификатор населенного пункта и составляющие адреса
        (страну, область, населенный пункт и район) по заданной строке.

        GET /location?term={term}"""
        raise NotImplementedError()

    def get_offer_intervals(self, station_id: str) -> dict:
        """Получение расписания вывозов в регионы. В качестве конечного пункта нужно указать либо geo_id (геоайди конечного региона),
        либо full_address (строковый конечный адрес), либо self_pickup_id (id пвз)"""
        raise NotImplementedError()

    def get_identifier(self, location: str) -> dict:
        """Получение идентификатора населённого пункта (geo_id) по адресу или его фрагменту.

        POST /api/b2b/platform/location/detect

        :params

        location - Адрес или его фрагмент (exm: "Москва, улица Тверская, 7")
        """
        raise NotImplementedError()

    def get_available_points_of_self_delivery(self,
                                              available_for_dropoff: bool = False,
                                              latitude: Dict[str, float] = None,
                                              longitude: Dict[str, float] = None,
                                              payment_method: str = None,
                                              payment_methods: List[str] = None,
                                              pickup_points_ids: List[str] = None,
                                              type: str = None) -> dict:
        """Получение списка точек самопривоза и самостоятельного получения заказа.
        Запрос для получения списка точек самопривоза и самостоятельного получения заказа.
        Может быть пустым, в этом случае вернутся все доступные точки.

        POST api/b2b/platform/pickup-points/list

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
        raise NotImplementedError()

    def pricing_calculator(self,
                           tariff: str,
                           total_weight: int,
                           source: Dict[str, str],
                           destination: Dict[str, str],
                           client_price: int = None,
                           payment_method: str = None,
                           total_assessed_price: int = None,
                           ) -> dict:
        """Расчет стоимости доставки на основании переданных параметров заказа.

        POST b2b-authproxy.taxi.yandex.net/api/b2b/platform/pricing-calculator

        tariff: Тариф доставки. Нужно выбрать 1 из 2.
        1) 'time_interval' - доставка до двери в интервал;
        2) 'self_pickup' - доствка до ПВЗ;

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

    def get_intervals(self,
                      station_id: str,
                      full_address: str = None,
                      geo_id: int = None,
                      self_pickup_id: str = None,
                      send_unix: bool = False,
                      last_mile_policy: str = 'time_interval') -> dict:
        """Получение расписания вывозов в регионы.
        В качестве конечного пункта нужно указать либо geo_id (геоайди конечного региона),
        либо full_address (строковый конечный адрес),
        либо self_pickup_id (id пвз)

        GET b2b-authproxy.taxi.yandex.net/api/b2b/platform/offers/info\
            ?station_id={string}\
            &full_address={string}\
            &geo_id={integer}\
            &self_pickup_id={string}\
            &send_unix={boolean}\
            &last_mile_policy={string}

        station_id - id станции (склада) отгрузки

        full_address - Полный конечный адрес доставки.

        geo_id - GeoID конечного адреса

        self_pickup_id - id пвз в логплатформе

        send_unix - Формат в котором время нужно отправить интервалы доставки (true - unix, false - utc)

        last_mile_policy - Требуемый способ доставки.
                           Значение по умолчанию: time_interval."""

        raise NotImplementedError()

    def confirm_order(self, offer_id: str):
        """Бронирование выбранного варианта доставки (оффера).

        POST b2b-authproxy.taxi.yandex.net/api/b2b/platform/offers/confirm

        offer_id - Идентификатор предложения маршрутного листа."""
        raise NotImplementedError()

    def get_offer_info(self, request_id: str, slim: bool = None):
        """Получение информации о заявке и ее текущем статусе.

        GET b2b-authproxy.taxi.yandex.net/api/b2b/platform/request/info\
            ?request_id={string}\
            &slim={boolean}

        request_id - ID заявки в логистической платформе

        slim - Флаг получения обновленной версии ответа."""
        raise NotImplementedError()

    def get_offers_info_in_interval(self,
                                    from_: Dict[Union[str, int]],
                                    to: Dict[Union[str, int]],
                                    requests_ids: list[str] = None):
        """МЕТОД ТЕСТИРУЕТСЯ.
        Получение информации о заявках, созданных в заданный временной интервал.

        POST b2b-authproxy.taxi.yandex.net/api/b2b/platform/requests/info

        from - Начало временного интервала создания заказов
        to - Конец временного интервала создания заказов
        requests_ids - Список идентификаторов заказов"""

    def edit_offer(self, ...):
        """Заявка на редактирование заказа"""
        raise NotImplementedError()

    def get_intervals_of_new_place(self):
        """Получение интервалов доставки для нового места получения заказа.

        POST b2b-authproxy.taxi.yandex.net/api/b2b/platform/request/redelivery_options"""
        raise NotImplementedError()

    def get_order_history(self, request_id: str) -> dict:
        """Получение информации об истории статусов заказа.

        GET b2b-authproxy.taxi.yandex.net/api/b2b/platform/request/history\
        ?request_id={string}

        request_id - ID заявки в логистической платформе"""
        raise NotImplementedError()

    def cancel_order(self, request_id: str) -> dict:
        """Отмена заявки, созданной в логистической платформе.

        POST b2b-authproxy.taxi.yandex.net/api/b2b/platform/request/cancel

        request_id - ID заявки в логистической платформе"""
        raise NotImplementedError()
