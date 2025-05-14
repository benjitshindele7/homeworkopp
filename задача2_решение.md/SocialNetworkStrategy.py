from abc import ABC, abstractmethod
from typing import List

class SocialNetworkStrategy(ABC):
    @abstractmethod
    def get_subscribers(self, user_name: str) -> List['SocialNetworkUser']:
        pass