public interface IDataSaveListener
{
    void OnDataSaved(object data);
}

public class DataSaveEventManager
{
    private readonly List<IDataSaveListener> _listeners = new List<IDataSaveListener>();

    public void Subscribe(IDataSaveListener listener) => _listeners.Add(listener);
    public void Notify(object data) => _listeners.ForEach(l => l.OnDataSaved(data));
}

public class MailListener : IDataSaveListener
{
    private readonly MailSender _sender;
    public MailListener(MailSender sender) => _sender = sender;
    public void OnDataSaved(object data) => _sender.Send("admin@example.com");
}

public class CacheListener : IDataSaveListener
{
    private readonly CacheUpdater _updater;
    public CacheListener(CacheUpdater updater) => _updater = updater;
    public void OnDataSaved(object data) => _updater.UpdateCache();
}

public class DatabaseSaverClient
{
    public void Main(bool b)
    {
        var eventManager = new DataSaveEventManager();
        eventManager.Subscribe(new MailListener(new MailSender()));
        eventManager.Subscribe(new CacheListener(new CacheUpdater()));

        var saver = new DatabaseSaver();
        DoSmth(saver, eventManager);
    }

    private void DoSmth(IDatabaseSaver saver, DataSaveEventManager manager)
    {
        saver.SaveData(null);
        manager.Notify(null);
    }
}