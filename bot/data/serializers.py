from marshmallow import Schema, fields


class LessonSchema(Schema):
    title = fields.Str()
    slug = fields.Str()


class ProductSchema(Schema):
    title = fields.Str()
    lesson = fields.Str()
    slug = fields.Str()
    price = fields.Decimal()
    link = fields.URL()


class CustomerSchema(Schema):
    tg_id = fields.Int(required=True)
    username = fields.Str()


class OrderSchema(Schema):
    product = fields.Nested(ProductSchema)
    customer = fields.Nested(CustomerSchema)
