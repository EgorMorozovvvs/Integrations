from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass()
class Item:
    """
    quantity: int - Количесто единиц товара

    size: {height: float, length: float, width: float} - Линейные размеры предмета в метрах.

    weight: float - Вес единицы товара в кг. В поле следует передавать актуальные значения.
                    Если вес не был передан, заказ считается оформленным на максимально допустимые габариты для тарифа.
                    Если фактические характеристики отправления превысят допустимые, курьер вправе отказаться
                    от выполнения такого заказа на месте. В этом случае будет удержана стоимость подачи.

                    Курьер (courier): до 10 кг Экспресс (express): до 20 кг Грузовой (cargo):

                    Маленький кузов: до 300 кг
                    Средний кузов: до 700 кг
                    Большой кузов: до 1400 кг

    cost_currency: RUB

    cost_value: Цена за штуку в валюте cost_currency. Для страхования стоимости передайте фактическую цену отправления

    droppof_point: Идентификатор точки, куда нужно доставить товар (отличается от идентификатора в заявке).
    Может быть любым числом. Должен соответствовать значению route_points[].point_id у точки назначения

    extra_id: Краткий уникальный идентификатор item'а (номер заказа в рамках заявки, как правило идентичен external_order_id)

    fiscalization: Информация по фискализации (актуально для оплаты при получении)

    pickup_point: Идентификатор точки, откуда нужно забрать товар (отличается от идентификатора в заявке).
    Может быть любым числом. Должен соответствовать значению route_points[].point_id у точки забора

    title: Наименование единицы товара
    """
    title: str
    quantity: int
    size: Dict[str, float]
    weight: float
    cost_currency: Optional[str] = None
    cost_value: Optional[str] = None
    droppof_point: Optional[int] = None
    extra_id: Optional[str] = None
    fiscalization: Optional[dict] = None
    pickup_point: Optional[int] = None

    def __post_init__(self):
        if any(key not in self.size for key in ['height', 'length', 'width']) and len(self.size) != 3:
            raise KeyError('Attribute "size" must be {height: float, length: float, width: float}')

@dataclass()
class RoutePoint:
    fullname: Optional[str] = None
    coordinates: Optional[list[float, float]] = None

    def __post_init__(self):
        if not(bool(self.fullname) or bool(self.coordinates)):
            raise ValueError('You must give although one argument')
