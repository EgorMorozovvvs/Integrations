from requests import get
from json import loads


url = 'https://robotapitest.dostavista.ru/api/business/1.3/'


def get_delivery_price(auth_token):
	return loads(get(
		url=url + 'calculate-order',
		headers={'X-DV-Auth-Token': auth_token}
	).text)
