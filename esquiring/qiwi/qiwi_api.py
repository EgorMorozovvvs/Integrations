import requests
from time import time


class Qiwi:
	""" Представляет собой кошелёк, на который принимаются платежи от пользователей сайта """

	__session: requests.Session
	__base_url: str
	phone: str

	def __init__(self, phone: str, api_token: str) -> None:
		"""
		:param str phone: № телефона, на который зарегистрирован аккаунт Qiwi, принимающий платежи
		:param str api_token: API-токен аккаунта Qiwi, принимающего платежи
		"""
		self.__session = requests.Session()
		self.__session.headers = {
			'content-type': 'application/json',
			'User-Agent': 'Android v3.2.0 MKT',
			'Accept': 'application/json',
			'Authorization': f'Bearer {api_token}'}
		self.phone = phone
		self.__base_url = 'https://edge.qiwi.com/'

	def get_balance(self) -> float:
		"""
		:return: Текущий баланс аккаунта, принимающего платежи
		"""
		response = self.__session.get(
			url=self.__base_url + f'funding-sources/v2/persons/{self.phone}/accounts'
		).json()
		balance = response['accounts'][0]['balance']['amount']
		return round(float(balance), 2)

	def transfer(
			self,
			wallet_address_to_transfer: str,
			transfer_amount: float,
			comment: str = '',
			currency: int = 643) -> dict:
		"""
		Совершает перевод средств от клиента сервису

		:param str wallet_address_to_transfer: адрес кошелька, с которого совершается перевод
		:param float transfer_amount: сумма перевода
		:param str comment: комментарий к переводу
		:param int currency: код валюты (по умолчанию - RUB)
		:return: Результат перевода
		"""
		transfer_amount = round(transfer_amount, 2)
		str_transfer_amount: str = str(transfer_amount)
		if '.' not in str_transfer_amount:
			str_transfer_amount += '.'
		while len(str_transfer_amount.split('.')[-1]) != 2:
			str_transfer_amount += '0'

		json = {
			'id': str(int(time() * 1000)),
			'sum': {
				'amount': str_transfer_amount,
				'currency': str(currency),
			},
			'paymentMethod': {
				'type': 'Account',
				'accountId': str(currency),
			},
			'comment': comment,
			'fields': {'account': wallet_address_to_transfer}
		}
		response = self.__session.post(
			url=self.__base_url + 'sinap/api/v2/terms/99/payments',
			json=json).json()
		return response
