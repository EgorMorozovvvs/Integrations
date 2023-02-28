from yandex_delivery.Dataclasses import *
from yandex_delivery.api import YandexDelivery

token = 'y2_AgAAAAD0Wcn4AAAPeAAAAAACJXtV-u9qs8IzQzWzJ0Cdt9pv-Wh1YS8'

yandex = YandexDelivery(token)

# items = [
#     Item(1, {'height': .5, 'length': .5, 'width': .5}, 2),
# ]
points = [
    RoutePoint(coordinates=[104.279560, 52.231710]),
    RoutePoint(coordinates=[104.090249, 52.210287])
]
cargo_options = ['auto_courier']

# a = yandex.check_price(items, points, cargo_options, '', 'courier')
# print(a)

# a = yandex.get_tariffs('Москва, Малая Андроньевская улица, 24', [37.673343823881204,55.74180656505421])
# print(a)

# a = yandex.find_full_address('Иркутск, Радужный')
# print(a)

# a = yandex.get_identifier('Иркутск, Радужный 33')
# print(a)

# a = yandex.get_available_points_of_self_delivery()
# print(a)

# a = yandex.preliminary_orders_assessment(tariff='self_pickup',
#                                          source={'platform_station_id': '4eb18cc4-329d-424d-a8a8-abfd8926463d'},
#                                          destination={'platform_station_id': 'fbbef9db-8243-452f-b096-3f9f869b3fe6'},
#                                          total_weight=100,
#                                          client_price=10000,
#                                          total_assessed_price=10000)
# print(a)

# a = yandex.get_intervals('4eb18cc4-329d-424d-a8a8-abfd8926463d',
#                          self_pickup_id='8716abcc-0faf-4efa-a89d-00125d845830')
# print(a)

a = yandex.find_full_address('Иркутск')
print(a)