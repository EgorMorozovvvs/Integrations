# from yandex_delivery import get_delivery_price
from crm.moysklad.moysklad import MoySklad
from esquiring.qiwi.qiwi_api import Qiwi


if __name__ == '__main__':
	q = Qiwi('zxc', 'zxc')
	q.get_balance()
	q.transfer('', 2.2, '')
