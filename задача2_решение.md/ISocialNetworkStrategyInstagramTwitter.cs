public class InstagramStrategy : ISocialNetworkStrategy
{
    public SocialNetworkUser[] GetSubscribers(string userName)
    {
        var client = new InstagramClient();
        var users = client.GetSubscribers(userName);
        return users.Select(u => new SocialNetworkUser { UserName = u.UserName }).ToArray();
    }
}

public class TwitterStrategy : ISocialNetworkStrategy
{
    public SocialNetworkUser[] GetSubscribers(string userName)
    {
        var client = new TwitterClient();
        long userId = client.GetUserIdByName(userName);
        var users = client.GetSubscribers(userId);
        return users.Select(u => new SocialNetworkUser 
                { 
                    UserName = client.GetUserNameById(u.UserId) 
                }).ToArray();
    }
}