import re

class TwitterUserService(UserService):
    def __init__(self):
        self.client = TwitterClient()
    
    def get_user_id(self, page_url: str) -> str:
        match = re.search(r"twitter.com/(\w+)", page_url)
        return match.group(1) if match else ""
    
    def get_user_name(self, user_id: str) -> str:
        return self.client.GetUserNameById(int(user_id))
    
    def get_friends(self, user_id: str) -> list['UserInfo']:
        subscribers = self.client.GetSubscribers(int(user_id))
        return [
            UserInfo(
                UserId=str(u.UserId),
                Name=self.client.GetUserNameById(u.UserId)
            ) for u in subscribers
        ]