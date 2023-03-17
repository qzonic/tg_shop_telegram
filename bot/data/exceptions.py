from requests.exceptions import ConnectionError


class BadConnectionToServer(ConnectionError):
    pass


class WrongHTTPAnswer(ValueError):
    pass


class Answer404Error(ValueError):
    pass
