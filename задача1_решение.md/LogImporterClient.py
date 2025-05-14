class LogImporterClient:
    def do_method(self):
        importer = LogImporter(FtpLogReader("user", "password"))
        importer.import_logs("log.txt")