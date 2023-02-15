from .handlers import unpack_items, unpack_route_points
from typing import Union


def create_order_template():
    template = {}
    return template


def check_price_template(**kwargs) -> dict:
    template = {
        'items': unpack_items(kwargs['items']),
        'requirements': {
            'cargo_loaders': kwargs['cargo_loaders'],
            'cargo_options': kwargs['cargo_options'],
            'cargo_type': kwargs['cargo_type'],
            'pro_courier': kwargs['pro_courier'],
            'taxi_class': kwargs['taxi_class'],
            'same_day_data': {
                'delivery_interval': {
                    'from': '2023-01-01T00:00:00+00:00', # need to get from user
                    'to': '2023-02-01T00:00:00+00:00', # also
                }
            }

        },
        'route_points': unpack_route_points(kwargs['route_points']),
        'skip_door_to_door': kwargs['skip_door_to_door']
    }
    return template
