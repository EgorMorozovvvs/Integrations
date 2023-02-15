from requests import get, post
from json import loads, dumps


url = 'https://b2b.taxi.tst.yandex.net/'
test_bearer = 'y2_AgAAAAD0Wcn4AAAPeAAAAAACJXtV-u9qs8IzQzWzJ0Cdt9pv-Wh1YS8'


def get_delivery_price():

	return loads(post(
		url=url + 'b2b/cargo/integration/v2/check-price',

		headers={
			'Authorization': f'Bearer {test_bearer}',
			'Accept-Language': 'ru'
		},

		data=dumps({

			'items': [{
				'quantity': 1,
				'size': {
					'height': 0.05,
					'length': 0.15,
					'width': 0.1
				},
				'weight': 2.105
			}],
			'requirements': {
				'cargo_loaders': 1,
				'cargo_options': ['thermobag'],
				'cargo_type': '1cv_m',
				'pro_courier': False,
				'same_day_data': {
					'delivery_interval': {
						'from': '2023-01-01T00:00:00+00:00',
						'to': '2023-02-01T00:00:00+00:00'
					}
				},
				'taxi_class': 'cargo'
			},
			'route_points': [
				{
					'coordinates': [0.063422, 0.028073],
				}
			],
			'skip_door_to_door': False
		})
	).text)
