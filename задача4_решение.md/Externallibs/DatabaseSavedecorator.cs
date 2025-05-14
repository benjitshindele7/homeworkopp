public class DatabaseSaverDecorator : IDatabaseSaver
{
    private readonly IDatabaseSaver _wrappedSaver;
    private readonly MailSender _mailSender;
    private readonly CacheUpdater _cacheUpdater;

    public DatabaseSaverDecorator(IDatabaseSaver saver, MailSender mailSender, CacheUpdater cacheUpdater)
    {
        _wrappedSaver = saver;
        _mailSender = mailSender;
        _cacheUpdater = cacheUpdater;
    }

    public void SaveData(object data)
    {
        _wrappedSaver.SaveData(data);
        _mailSender.Send("admin@example.com");
        _cacheUpdater.UpdateCache();
    }
}

// Клиентский код
public class DatabaseSaverClient
{
    public void Main(bool b)
    {
        var saver = new DatabaseSaverDecorator(
            new DatabaseSaver(),
            new MailSender(),
            new CacheUpdater()
        );
        DoSmth(saver);
    }

    private void DoSmth(IDatabaseSaver saver)
    {
        saver.SaveData(null);
    }
}