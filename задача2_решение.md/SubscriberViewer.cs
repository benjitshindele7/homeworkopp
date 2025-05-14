public class SubscriberViewer
{
    private readonly Dictionary<SocialNetwork, ISocialNetworkStrategy> _strategies;

    public SubscriberViewer()
    {
        _strategies = new Dictionary<SocialNetwork, ISocialNetworkStrategy>
        {
            { SocialNetwork.Instagram, new InstagramStrategy() },
            { SocialNetwork.Twitter, new TwitterStrategy() }
        };
    }

    public SocialNetworkUser[] GetSubscribers(string userName, SocialNetwork networkType)
    {
        if (!_strategies.TryGetValue(networkType, out var strategy))
            throw new ArgumentException("Unsupported social network");

        return strategy.GetSubscribers(userName);
    }
}