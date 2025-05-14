from abc import ABC, abstractmethod

class DataSaveListener(ABC):
    @abstractmethod
    def on_data_saved(self, data):
        pass

class DataSaveEventManager:
    def __init__(self):
        self._listeners = []
    
    def subscribe(self, listener):
        self._listeners.append(listener)
    
    def notify(self, data):
        for listener in self._listeners:
            listener.on_data_saved(data)

class MailListener(DataSaveListener):
    def __init__(self, mail_sender):
        self._mail_sender = mail_sender
    
    def on_data_saved(self, data):
        self._mail_sender.send("admin@example.com")

class CacheListener(DataSaveListener):
    def __init__(self, cache_updater):
        self._cache_updater = cache_updater
    
    def on_data_saved(self, data):
        self._cache_updater.update_cache()

class DatabaseSaverClient:
    def main(self, b):
        event_manager = DataSaveEventManager()
        event_manager.subscribe(MailListener(MailSender()))
        event_manager.subscribe(CacheListener(CacheUpdater()))

        saver = DatabaseSaver()
        self.do_smth(saver, event_manager)

    def do_smth(self, saver, event_manager):
        saver.save_data(None)
        event_manager.notify(None)