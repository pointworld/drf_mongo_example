from mongoengine import Document, fields


class Poll(Document):
    name = fields.StringField(required=True)
    votes = fields.IntField(required=True)
