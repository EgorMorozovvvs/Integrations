import datetime
import hashlib
from typing import Dict, Union
from xml.etree import ElementTree
from xml.etree.ElementTree import tostring
from boltons.iterutils import remap


ARRAY_TAGS = {'State', 'Delay', 'Good', 'Fail', 'Item', 'Package'}


def xml_to_dict(xml: ElementTree) -> Dict:
	result = xml.attrib
	for child in xml:
		if child.tag in ARRAY_TAGS:
			result[child.tag] = result.get(child.tag, [])
			result[child.tag].append(xml_to_dict(child))
		else:
			result[child.tag] = xml_to_dict(child.tag)
	return result


def get_secure(secure_password: str, date: Union[datetime.datetime, datetime.date, str]) -> str:
	"""
	Генерация секретного кода для запросов, требующих авторизации

	:param secure_password: пароль для интеграции со СДЭК

	:param date: дата документа

	:return: секретный код
	"""
	code = f'{date}&{secure_password}'.encode('utf-8')
	return hashlib.md5(code).hexdigest()


def clear_dict(data: Dict) -> Dict:
	"""
		Очистка словаря от ключей со значением None

		:param data: исходный словарь

		:return: очищенный словарь
		"""
	return remap(data, lambda p, k, v: v is not None)


def prepare_xml(data: Dict) -> Dict:
	data = clear_dict(data)
	data = remap(data, lambda p, k, v: (k, str(v)))
	return data


def xml_to_string(xml: ElementTree) -> str:
	tree = ElementTree.ElementTree(xml)
	for elem in tree.iter():
		elem.attrib = prepare_xml(elem.attrib)
	return tostring(tree.getroot(), encoding='UTF-8')
