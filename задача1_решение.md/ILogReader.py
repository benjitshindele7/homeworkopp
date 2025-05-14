class ILogReader:
    def read_log_file(self, identificator: str) -> str:
        pass

class FtpLogReader(ILogReader):
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.ftp_client = FtpClient()

    def read_log_file(self, file_path: str) -> str:
        return self.ftp_client.read_file(self.login, self.password, file_path)