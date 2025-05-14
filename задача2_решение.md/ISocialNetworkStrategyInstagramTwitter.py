class InstagramStrategy(SocialNetworkStrategy):
    def get_subscribers(self, user_name: str) -> List['SocialNetworkUser']:
        from ExternalLibs.Instagram import InstagramClient, InstagramUser
        
        client = InstagramClient()
        users = client.GetSubscribers(user_name)
        return [SocialNetworkUser(user.UserName) for user in users]

class TwitterStrategy(SocialNetworkStrategy):
    def get_subscribers(self, user_name: str) -> List['SocialNetworkUser']:
        from ExternalLibs.Twitter import TwitterClient, TwitterUser
        
        client = TwitterClient()
        user_id = client.GetUserIdByName(user_name)
        subscribers = client.GetSubscribers(user_id)
        return [SocialNetworkUser(client.GetUserNameById(u.UserId)) for u in subscribers]