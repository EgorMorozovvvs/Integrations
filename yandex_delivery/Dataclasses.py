from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass()
class Item:
    """
    quantity: int - Количесто единиц товара
    size: {height: float, length: float, width: float} - Линейные размеры предмета в метрах.
    weight: float - Вес в килограммах
    """
    quantity: int
    size: Dict[str, float]
    weight: float

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
