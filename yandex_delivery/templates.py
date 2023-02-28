from .utils import unpack_items, unpack_route_points, pop_if_value_none


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
                    'from': '2023-01-01T00:00:00+00:00',
                    'to': '2023-02-01T00:00:00+00:00',
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


@pop_if_value_none
def get_available_points_of_self_delivery_template(**kwargs) -> dict:
    template = {
        'available_for_dropoff': kwargs['available_for_dropoff'],
        'latitude': kwargs['latitude'],
        'longitude': kwargs['longitude'],
        'payment_method': kwargs['payment_method'],
        'payment_methods': kwargs['payment_methods'],
        'pickup_points_ids': kwargs['pickup_points_ids'],
        'type': kwargs['type']
    }

    return template


def pricing_calculator_template(**kwargs) -> dict:
    template = {
        'client_price': kwargs['client_price'],
        'destination': kwargs['destination'],
        'payment_method': kwargs['payment_method'],
        'source': kwargs['source'],
        'tariff': kwargs['tariff'],
        'total_assessed_price': kwargs['total_assessed_price'],
        'total_weight': kwargs['total_weight']
    }
    return template


def create_order_template(**kwargs) -> dict:
    template = {
        'billing_info': {
            'delivery_cost': int,
            'payment_method': str,
        },
        'destination': {
            'custom_location': {
                'details': {
                    'comment': str,
                    'full_address': str,
                    'room': str,
                },
                'latitude': float,
                'longitude': float,
            },
            'interval': {
                'from': float,
                'to': float
            },
            'interval_utc': {
                'from': str,
                'to': str
            },
            'platform_station': {
                'platform_id': str
            },
            'type': str
        },
        'info': {
            'comment': str,
            'operator_request_id': str
        },
        'items': [
            {
                'article': str,
                'billing_details': {
                    'assessed_unit_price': int,
                    'inn': str,
                    'nds': int,
                    'unit_price': int
                },
                'count': int,
                'making_code': str,
                'name': str,
                'physical_dims': {
                    'dx': int,
                    'dy': int,
                    'dz': int
                },
                'place_barcode': str,
                'uin': str
            }
        ],
        'last_mile_policy': str,
        'particular_items_refuse': bool,
        'places': [
            {
                'barcode': str,
                'description': str,
                'physical_dims': {
                    'dx': int,
                    'dy': int,
                    'dz': int,
                    'predefined_volume': int,
                    'weight_gross': int
                }
            }
        ],
        'recipient_info': {
            'email': str,
            'first_name': str,
            'last_name': str,
            'partonymic': str,
            'phone': str
        },
        'source': {
            'platform_station': {
                'platform_id': str
            }
        }
    }
    return template


def get_intervals_of_new_place_template(**kwargs) -> dict:
    template = {
        'destination': {
            'custom_location': {
                'details': {
                    'comment': str,
                    'full_address': str,
                    'room': str
                },
                'latitude': float,
                'longitude': float
            },
            'interval': {
                'from': int,
                'to': int
            },
            'interval_utc': {
                'from': int,
                'to': int
            },
            'platform_station': {
                'platform_id': str
            },
            'type': str
        },
        'request_id': str
    }
    return template


def cancel_order_template(**kwargs) -> dict:
    template = {
        'request_id': kwargs['request_id']
    }
    return template
