using Patterns.Ex00.ExternalLibs;

namespace Patterns.Ex00
{
    public class FtpLogReader : ILogReader
    {
        private readonly string _login;
        private readonly string _password;
        private readonly FtpClient _ftpClient;

        public FtpLogReader(string login, string password)
        {
            _login = login;
            _password = password;
            _ftpClient = new FtpClient();
        }

        public string ReadLogFile(string filePath)
        {
            return _ftpClient.ReadFile(_login, _password, filePath);
        }
    }
}