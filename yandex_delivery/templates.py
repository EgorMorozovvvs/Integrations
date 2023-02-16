from typing import Union
from .utils import unpack_items, unpack_route_points


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
                    'from': '2023-01-01T00:00:00+00:00',  # need to get from user
                    'to': '2023-02-01T00:00:00+00:00',  # also
                }
            }

        },
        'route_points': unpack_route_points(kwargs['route_points']),
        'skip_door_to_door': kwargs['skip_door_to_door']
    }
    return template


def get_intervals_during_day_template(**kwargs) -> dict:
    template = {
        'fullname': kwargs['fullname'],
        'start_point': kwargs['start_point'],
    }
    return template


def get_tariffs_template(**kwargs) -> dict:
    template = {
        'fullname': kwargs['fullname'],
        'start_point': kwargs['start_point'],
    }
    return template


def search_ways_of_delivery_templates(**kwargs) -> dict:
    template = {
        'senderId': kwargs['sender_id'],
        'from': kwargs['from'],
        'to': kwargs['to'],
        'dimensions': ...,
        'places': [
            {
                'dimensions': {
                    'length': float,
                    'width': float,
                    'height': float,
                    'weight': float
                },
            },
            ...
        ],
        'deliveryType': kwargs['delivery_type'],
        'shipment': {
            'date': str,
            'type': str,
            'partnerId': int,
            'warehouseId': int,
            'includeNonDefault': bool
        },
        'cost': {
            'assessedValue': float,
            'itemsSum': float,
            'manualDeliveryForCustomer': float,
            'fullyPrepaid': bool
        },
        'settings': {
            'useHandlingTime': bool,
            'useWarehousesSchedule': bool,
            'showDisabledOptions': bool,
        },
        'tariffId': int,
        'desiredDeliveryDate': str
    }
    return template
