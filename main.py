# from yandex_delivery import get_delivery_price
from crm.moysklad.moysklad import MoySklad


if __name__ == '__main__':
	ms = MoySklad()
	ms.authorize(login='', password='')
	print(ms.get_assortment())
