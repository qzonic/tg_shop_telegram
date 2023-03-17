from decimal import Decimal
from dataclasses import dataclass


@dataclass
class LessonModel:
    title: str
    slug: str
    full_title: str


@dataclass
class ProductModel:
    title: str
    lesson: str
    slug: str
    price: Decimal
    link: str


@dataclass
class CustomerModel:
    tg_id: int
    username: str


@dataclass
class OrderModel:
    product: ProductModel
    customer: CustomerModel
