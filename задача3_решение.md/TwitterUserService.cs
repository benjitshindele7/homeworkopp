public class TwitterUserService : UserService
{
    private readonly TwitterClient _client = new TwitterClient();

    protected override string GetUserId(string pageUrl)
    {
        var regex = new Regex("twitter.com/(.*)");
        return regex.Match(pageUrl).Groups[1].Value;
    }

    protected override string GetUserName(string userId)
    {
        return _client.GetUserNameById(long.Parse(userId));
    }

    protected override UserInfo[] GetFriends(string userId)
    {
        var subscribers = _client.GetSubscribers(long.Parse(userId));
        return subscribers.Select(u => new UserInfo 
        {
            UserId = u.UserId.ToString(),
            Name = _client.GetUserNameById(u.UserId)
        }).ToArray();
    }
}
