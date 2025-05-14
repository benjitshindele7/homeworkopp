class TwitterUser:
    """Этот класс нельзя менять по условиям задания
    В реальном проекте такой класс скорее всего будет в составе базовой библиотеки, 
    доступа к изменению которого не будет
    """
    def __init__(self, user_id: int = 0):
        self.UserId = user_id  # Сохранение оригинального имени поля из C#

class TwitterClient:
    """Этот класс нельзя менять по условиям задания
    В реальном проекте такой класс скорее всего будет в составе базовой библиотеки, 
    доступа к изменению которого не будет
    """
    
    def GetUserIdByName(self, name: str) -> int:
        """Аналог метода из C#: public long GetUserIdByName(string name)"""
        # Заглушка как в оригинале: return 1
        return 1
    
    def GetUserNameById(self, user_id: int) -> str:
        """Аналог метода из C#: public String GetUserNameById(long id)"""
        # Заглушка как в оригинале: return ""
        return ""
    
    def GetSubscribers(self, user_id: int) -> list[TwitterUser]:
        """Аналог метода из C#: public TwitterUser[] GetSubscribers(long userId)"""
        # Заглушка как в оригинале: return new TwitterUser[0]
        return []