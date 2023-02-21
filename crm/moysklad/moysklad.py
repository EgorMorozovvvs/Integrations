# API docs: https://dev.moysklad.ru/doc/api/remap/1.2/#mojsklad-json-api


import base64
import requests


class MoySklad:
	""" Реализует взаимодействие с платформой "МойСклад" """

	__access_token: str
	__credentials: str
	__url: str

	def __init__(self) -> None:
		self.__access_token = ''
		self.__credentials = ''
		self.__url = 'https://online.moysklad.ru/api/remap/1.2/'

	def authorize(self, login: str, password: str) -> None:
		"""
		:param str login: Логин пользователя
		:param str password: Пароль пользователя

		Получает токен доступа для логина и пароля для дальнейших взаимодействий
		"""
		self.__credentials = base64.b64encode(bytes(f'{login}:{password}'.encode('ascii'))).decode('utf-8')
		data = requests.post(
			url=self.__url + 'security/token',
			headers={'Authorization': f'Basic {self.__credentials}'}
		).json()
		if 'errors' in data.keys():
			raise Exception(data['errors'][0]['error'])
		self.__access_token = data['access_token']

	def get_advanced_leftovers_report(self) -> dict:
		""" Возвращает расширенный отчёт об остатках """
		data = requests.get(
			url=self.__url + 'report/stock/all',
			headers={'Authorization': f'Bearer {self.__access_token}'}
		).json()
		return data

	def get_leftovers_cutaway_report(self) -> dict:
		""" Возвращает остаток в разрезе """
		data = requests.get(
			url=self.__url + 'report/stock/bystore',
			headers={'Authorization': f'Bearer {self.__access_token}'}
		).json()
		return data

	def get_assortment(self) -> dict:
		""" Возвращает ассортимент склада пользователя """
		data = requests.get(
			url=self.__url + 'entity/assortment',
			headers={'Authorization': f'Bearer {self.__access_token}'}
		).json()

		return data

	def get_country_list(self):
		data = requests.get(
			url=self.__url + 'entity/country',
			headers={'Authorization': f'Bearer {self.__access_token}'}
		).json()
		return data
