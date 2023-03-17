from bot import config
from .managers import BaseManager
from .serializers import (
    LessonSchema,
    ProductSchema,
    CustomerSchema,
    OrderSchema
)


class LessonQuery:
    GET_URL = config.HOST + 'lessons/{0}/'
    ALL_URL = config.HOST + 'lessons/'
    SCHEMA = LessonSchema()
    objects = BaseManager(
        get_url=GET_URL,
        all_url=ALL_URL,
        schema=SCHEMA
    )


class ProductQuery:
    GET_URL = config.HOST + 'lessons/{0}/products/{1}/'
    ALL_URL = config.HOST + 'lessons/{0}/products/'
    SCHEMA = ProductSchema()
    objects = BaseManager(
        get_url=GET_URL,
        all_url=ALL_URL,
        schema=SCHEMA
    )


class CustomerQuery:
    GET_URL = config.HOST + 'customers/{0}/'
    CREATE_URL = config.HOST + 'customers/'
    SCHEMA = CustomerSchema()
    objects = BaseManager(
        get_url=GET_URL,
        create_url=CREATE_URL,
        schema=SCHEMA
    )


class OrderQuery:
    ALL_URL = config.HOST + 'orders/{0}/'
    CREATE_URL = ALL_URL
    SCHEMA = OrderSchema()
    objects = BaseManager(
        all_url=ALL_URL,
        create_url=CREATE_URL,
        schema=SCHEMA
    )
