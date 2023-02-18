import base64
import requests
import json


class MoySklad:
	""" Реализует взаимодействие с платформой "МойСклад" """

	access_token: str
	credentials: str
	url: str

	def __init__(self) -> None:
		self.access_token = ''
		self.credentials = ''
		self.url = 'https://online.moysklad.ru/api/remap/1.2/'

	def authorize(self, login: str, password: str) -> None:
		""" Получает токен доступа для логина и пароля для дальнейших взаимодействий """
		self.credentials = base64.b64encode(bytes(f'{login}:{password}'.encode('ascii'))).decode('utf-8')
		data = requests.post(
			url=self.url + 'security/token',
			headers={'Authorization': f'Basic {self.credentials}'}
		).json()
		if 'errors' in data.keys():
			raise Exception(data['errors'][0]['error'])
		self.access_token = data['access_token']

	def get_advanced_leftovers_report(self):
		""" Возвращает расширенный отчёт об остатках """
		data = requests.get(
			url=self.url + 'report/stock/all',
			headers={'Authorization': f'Bearer {self.access_token}'}
		).json()
		return data

	def get_leftovers_cutaway_report(self):
		""" Возвращает остаток в разрезе """
		data = requests.get(
			url=self.url + 'report/stock/bystore',
			headers={'Authorization': f'Bearer {self.access_token}'}
		).json()
		return data

	def get_assortment(self):
		""" Возвращает ассортимент """
		data = requests.get(
			url=self.url + 'entity/assortment',
			headers={'Authorization': f'Bearer {self.access_token}'}
		).json()
		return data
