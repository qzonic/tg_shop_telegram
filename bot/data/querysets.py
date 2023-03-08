import requests

from bot import config
# from . import exceptions
from serializers import (
    LessonSchema,
    ProductSchema,
    CustomerSchema,
    OrderSchema
)


class BaseModel:
    GET_URL = config.HOST
    CREATE_URL = config.HOST
    ALL_URL = config.HOST

    @staticmethod
    def make_headers():
        return {
            'Authorization': f'{config.SITE_TOKEN}'
        }

    @classmethod
    def make_response(cls, *args, url=None, method='GET', **kwargs):
        arguments = {
            'url': url.format(*args),
            'headers': cls.make_headers(),
        }
        try:
            if method == 'POST':
                arguments['data'] = {**kwargs}
                request = requests.post(**arguments)
            else:
                request = requests.get(**arguments)
            return request
        except requests.exceptions.ConnectionError as error:
            message = f'Ошибка запроса к API: {error}'
            raise exceptions.BadConnectionToServer(message)

    @staticmethod
    def check_status(response, status_code):
        if response.status_code != status_code:
            message = (f'При {response.request.method}-запросе на эндроинт "{response.url}" '
                       f'вернулся статус отличный от {status_code} ==> {response.status_code}!!!')
            raise exceptions.WrongHTTPAnswer(message)
        return True

    @classmethod
    def get(cls, *args):
        response = cls.make_response(url=cls.GET_URL, *args)
        status_code = cls.check_status(
            response,
            HTTPStatus.OK
        )
        if isinstance(status_code, bool):
            return response.json()

    @classmethod
    def all(cls, *args):
        response = cls.make_response(url=cls.ALL_URL, *args)
        status_code = cls.check_status(
            response,
            HTTPStatus.OK
        )
        if isinstance(status_code, bool):
            return response.json()

    @classmethod
    def create(cls, *args, **kwargs):
        response = cls.make_response(url=cls.CREATE_URL, method='POST', *args, **kwargs)
        status_code = cls.check_status(
            response,
            HTTPStatus.CREATED
        )
        if isinstance(status_code, bool):
            return response.json()
        return status_code


class CustomerModel(BaseModel):
    GET_URL = HOST + 'customers/{0}/'
    CREATE_URL = HOST + 'customers/'

    @staticmethod
    def check_status(response, status_code):
        if response.status_code not in (status_code, status.HTTP_404_NOT_FOUND):
            message = (f'При {response.request.method}-запросе на эндроинт "{response.url}" '
                       f'вернулся статус отличный от {status_code} ==> {response.status_code}!!!')
            logging.error(message)
            raise exceptions.WrongHTTPAnswer(message)
        elif response.status_code == HTTPStatus.NOT_FOUND:
            message = f'Пользователь не найден, перехожу к его созданию!'
            # raise exceptions.Answer404Error(message)
        return True

    # @classmethod
    # def get_or_create(cls, **kwargs):
    #     try:
    #         response = cls.get(kwargs['tg_id'])
    #     except exceptions.Answer404Error:
    #         response = cls.create(**kwargs)
    #     return response


class LessonModel(BaseModel):
    GET_URL = config.HOST + 'lessons/{0}/'
    ALL_URL = config.HOST + 'lessons/'


class ProductModel(BaseModel):
    GET_URL = config.HOST + 'lessons/{0}/products/{1}/'
    ALL_URL = config.HOST + 'lessons/{0}/products/'


class OrderModel(BaseModel):
    ALL_URL = config.HOST + 'orders/{0}/'
    CREATE_URL = config.HOST + 'orders/{0}/'


