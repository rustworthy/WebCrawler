from abc import ABC, abstractmethod
from typing import Optional, Union, Any, Dict, List


class BaseCrudExecutor(ABC):
    @abstractmethod
    def insert(self, post: str) -> str:
        pass

    @abstractmethod
    def find(self, unique_id: str = None) -> Union[Dict[str, Any], List[Dict[str, Any]], None]:
        pass

    @abstractmethod
    def update(self, data: Dict[str, Any]) -> Optional[bool]:
        pass

    @abstractmethod
    def delete(self, unique_id: str) -> Optional[bool]:
        pass

    @abstractmethod
    def insert_all_remaining(self, posts: List[str]) -> None:
        pass
