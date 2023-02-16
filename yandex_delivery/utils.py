from typing import List
from .Dataclasses import Item, RoutePoint


def unpack_items(items: List[Item]) -> list[dict]:
    return [{'quantity': item.quantity,
             'size': item.size,
             'weight': item.weight} for item in items]


def unpack_route_points(route_points: List[RoutePoint]) -> list[dict]:
    return [{'coordinates': point.coordinates if point.coordinates else [],
             'fullname': point.fullname if point.fullname else ''} for point in route_points]
