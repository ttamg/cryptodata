from mongoengine import Document, connect, FloatField, StringField, DictField, ListField

from config import DATABASE

connect(DATABASE, host='localhost', port=27017)


class Ticker(Document):
    """
    Document to store ticker information
    """
    unixtime = FloatField(required=True, )
    exchange = StringField(required=True, max_length=20)
    pair = StringField(required=True, max_length=10)
    content = DictField(required=True)


class Orderbook(Document):
    """
    Document to store orderbook information
    """
    unixtime = FloatField(required=True, )
    exchange = StringField(required=True, max_length=20)
    pair = StringField(required=True, max_length=10)
    content = DictField(required=True)


class Trades(Document):
    """
    Document to store recent trades information
    """
    unixtime = FloatField(required=True, )
    exchange = StringField(required=True, max_length=20)
    pair = StringField(required=True, max_length=10)
    content = ListField(required=True)
