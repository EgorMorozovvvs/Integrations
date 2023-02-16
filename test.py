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

# a = yandex.find_full_address('Иркутск')
# print(a)

# a = yandex.get_identifier('Иркутск')
# print(a)

a = yandex.get_available_points_of_self_delivery()
for i in a.values():
    print(i)