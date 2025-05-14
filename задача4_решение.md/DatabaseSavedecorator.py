class DatabaseSaverDecorator:
    def __init__(self, saver, mail_sender, cache_updater):
        self._saver = saver
        self._mail_sender = mail_sender
        self._cache_updater = cache_updater

    def save_data(self, data):
        self._saver.save_data(data)
        self._mail_sender.send("admin@example.com")
        self._cache_updater.update_cache()

# Клиентский код
class DatabaseSaverClient:
    def main(self, b):
        saver = DatabaseSaverDecorator(
            DatabaseSaver(),
            MailSender(),
            CacheUpdater()
        )
        self.do_smth(saver)

    def do_smth(self, saver):
        saver.save_data(None)