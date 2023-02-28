from typing import List, Iterable
from .Dataclasses import Item, RoutePoint


def unpack_items(items: List[Item]) -> list[dict]:
    return [{'quantity': item.quantity,
             'size': item.size,
             'weight': item.weight} for item in items]


def unpack_route_points(route_points: List[RoutePoint]) -> list[dict]:
    return [{'coordinates': point.coordinates if point.coordinates else [],
             'fullname': point.fullname if point.fullname else ''} for point in route_points]


def calc_dimensions(items: Iterable[Item]):
    dimension = {
        'length': sum(i.size['length'] for i in items),
        'width': sum(i.size['width'] for i in items),
        'height': sum(i.size['height'] for i in items),
        'weight': sum(i.weight for i in items)
    }


def pop_if_value_none(func):
    def inner(**kwargs):
        template = func(**kwargs)
        for key in kwargs:
            if kwargs[key] is None:
                template.pop(key)
        return template

    return inner
