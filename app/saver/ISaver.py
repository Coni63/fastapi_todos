from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import IItem


class ISaver(ABC):
    @abstractmethod
    def save(self, item: 'IItem') -> bool:
        pass

    @abstractmethod
    def get_all_items(self) -> list['IItem']:
        pass

    @abstractmethod
    def update(self, item: 'IItem') -> 'IItem':
        pass
