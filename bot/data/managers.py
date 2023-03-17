import status
import logging
import requests

from bot import config
from bot.data import exceptions
from bot.handlers import messages


class BaseManager:

    LOGGER = logging.getLogger(__name__)

    def __init__(
            self,
            get_url: str=None,
            all_url: str=None,
            create_url: str=None,
            schema=None
    ) -> None:
        self.get_url = get_url
        self.all_url = all_url
        self.create_url = create_url
        self.schema = schema

    @staticmethod
    def headers():
        return {
            'Authorization': f'{config.SITE_TOKEN}'
        }

    def make_response(self, *args, url=None, method='GET', **kwargs):
        arguments = {
            'url': url.format(*args),
            'headers': self.headers(),
        }
        try:
            if method == 'POST':
                arguments['data'] = {**kwargs}
                request = requests.post(**arguments)
            else:
                request = requests.get(**arguments)
            return request
        except requests.exceptions.RequestException as error:
            message = messages.API_ERROR.format(error)
            self.LOGGER.critical(message)
            raise exceptions.BadConnectionToServer(message)

    def check_status(self, response, status_code):
        if response.status_code != status_code:
            message = messages.WRONG_HTTP_EXCEPTION.format(
                response.request.method,
                response.url,
                status_code,
                response.status_code
            )
            self.LOGGER.error(message)
            return response.status_code
        return True

    def get(self, *args):
        response = self.make_response(
            url=self.get_url,
            *args
        )
        status_code = self.check_status(response, status.HTTP_200_OK)
        if isinstance(status_code, bool):
            return self.schema.load(response.json())
        else:
            return status_code

    def all(self, *args):
        response = self.make_response(
            url=self.all_url,
            *args
        )
        status_code = self.check_status(response, status.HTTP_200_OK)
        if isinstance(status_code, bool):
            return self.schema.load(response.json(), many=True)
        else:
            return status_code

    def create(self, *args, **kwargs):
        response = self.make_response(
            url=self.create_url,
            method='POST',
            *args,
            **kwargs
        )
        status_code = self.check_status(response, status.HTTP_201_CREATED)
        if isinstance(status_code, bool):
            return self.schema.load(response.json())
        else:
            return status_code

    def connection_test(self):
        return self.make_response(url=config.HOST)
