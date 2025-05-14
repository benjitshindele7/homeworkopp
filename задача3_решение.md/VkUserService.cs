public class VkUserService : UserService
{
    protected override string GetUserId(string pageUrl)
    {
        return new VkUserService().Parse(pageUrl);
    }

    protected override string GetUserName(string userId)
    {
        return new VkUserService().GetName(userId);
    }

    protected override UserInfo[] GetFriends(string userId)
    {
        var users = new VkUserService().GetFriendsById(userId);
        return new VkUserService().ConvertToUserInfo(users);
    }
}