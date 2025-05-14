namespace Patterns.Ex00
{
    public class LogImporterClient
    {
        public void DoMethod()
        {
            // Передаем логин, пароль и путь к файлу на FTP
            LogImporter importer = new LogImporter(new FtpLogReader("user", "password"));
            importer.ImportLogs("log.txt"); // Путь к файлу на сервере
        }
    }
}