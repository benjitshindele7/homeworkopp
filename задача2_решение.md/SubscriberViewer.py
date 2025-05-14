from enum import Enum

class SocialNetwork(Enum):
    Instagram = 1
    Twitter = 2

class SubscriberViewer:
    def __init__(self):
        self._strategies = {
            SocialNetwork.Instagram: InstagramStrategy(),
            SocialNetwork.Twitter: TwitterStrategy()
        }
    
    def get_subscribers(self, user_name: str, network_type: SocialNetwork) -> List['SocialNetworkUser']:
        strategy = self._strategies.get(network_type)
        if not strategy:
            raise ValueError("Unsupported social network")
        return strategy.get_subscribers(user_name)