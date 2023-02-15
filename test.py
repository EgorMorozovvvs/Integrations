from yandex_delivery.Dataclasses import *
from yandex_delivery.main import YandexDelivery

token = 'y2_AgAAAAD0Wcn4AAAPeAAAAAACJXtV-u9qs8IzQzWzJ0Cdt9pv-Wh1YS8'

yandex = YandexDelivery(token)

items = [Item(1, {'height': 1.0, 'length': 1.0, 'width': 1.0}, 2)]
points = [RoutePoint(coordinates=[30.308868, 59.928478]), RoutePoint(coordinates=[30.354538, 59.919280])]
cargo_options = ['auto_courier']

a = yandex.check_price(items, points, cargo_options, 'lcv_m', 'express')
print(a)
