from marshmallow import Schema, fields, post_load

from . import models


class MainSchema(Schema):
    model = None

    @post_load
    def make_user(self, data, **kwargs):
        return self.model(**data)


class LessonSchema(MainSchema):
    title = fields.Str()
    slug = fields.Str()
    full_title = fields.Str()

    model = models.LessonModel


class ProductSchema(MainSchema):
    title = fields.Str()
    lesson = fields.Str()
    slug = fields.Str()
    price = fields.Decimal()
    link = fields.URL()

    model = models.ProductModel


class CustomerSchema(MainSchema):
    tg_id = fields.Int(required=True)
    username = fields.Str()

    model = models.CustomerModel


class OrderSchema(MainSchema):
    product = fields.Nested(ProductSchema)
    customer = fields.Nested(CustomerSchema)

    model = models.OrderModel
