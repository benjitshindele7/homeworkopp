public abstract class UserService
{
    public UserInfo GetUserInfo(string pageUrl)
    {
        // 1. Получение идентификатора и имени пользователя
        var userId = GetUserId(pageUrl);
        var userName = GetUserName(userId);

        // 2. Получение друзей
        var friends = GetFriends(userId);

        // 3. Сборка результата
        return new UserInfo
        {
            UserId = userId,
            Name = userName,
            Friends = friends
        };
    }

    protected abstract string GetUserId(string pageUrl);
    protected abstract string GetUserName(string userId);
    protected abstract UserInfo[] GetFriends(string userId);
}
