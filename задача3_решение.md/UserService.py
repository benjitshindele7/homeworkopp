from abc import ABC, abstractmethod

class UserService(ABC):
    def get_user_info(self, page_url: str) -> 'UserInfo':
        # 1. Получение идентификатора и имени
        user_id = self.get_user_id(page_url)
        user_name = self.get_user_name(user_id)
        
        # 2. Получение друзей
        friends = self.get_friends(user_id)
        
        # 3. Сборка результата
        return UserInfo(
            UserId=user_id,
            Name=user_name,
            Friends=friends
        )
    
    @abstractmethod
    def get_user_id(self, page_url: str) -> str:
        pass
    
    @abstractmethod
    def get_user_name(self, user_id: str) -> str:
        pass
    
    @abstractmethod
    def get_friends(self, user_id: str) -> list['UserInfo']:
        pass