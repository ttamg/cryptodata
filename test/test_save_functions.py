from config import EXCHANGES
from cryptodata.save_ticker import save_ticker
from cryptodata.save_orderbook import save_orderbook
from cryptodata.save_trades import save_trades

from mongo.mongo import Ticker, Orderbook, Trades

"Unixtime set so that this can be deleted easily"
unixtime = 100.0


def test_save_ticker():
    """Test that we get responses from the exchange"""
    api = EXCHANGES[0]['api']
    pair = EXCHANGES[0]['pairs'][0]
    name = EXCHANGES[0]['name']
    count = Ticker.objects.count()
    record, response = save_ticker(api=api, pair=pair, name=name, unixtime=unixtime)
    assert type(response) == dict
    assert record.exchange == name
    assert record.unixtime == unixtime
    assert record.pair == pair[0]
    assert record.content == response
    assert Ticker.objects.count() == count+1


def test_save_orderbook():
    """Test that we get responses from the exchange"""
    api = EXCHANGES[1]['api']
    pair = EXCHANGES[1]['pairs'][0]
    name = EXCHANGES[1]['name']
    count = Orderbook.objects.count()
    record, response = save_orderbook(api=api, pair=pair, name=name, unixtime=unixtime)
    assert type(response) == dict
    assert record.exchange == name
    assert record.unixtime == unixtime
    assert record.pair == pair[0]
    assert record.content == response
    assert Orderbook.objects.count() == count+1


def test_save_trades():
    """Test that we get responses from the exchange"""
    api = EXCHANGES[2]['api']
    pair = EXCHANGES[2]['pairs'][0]
    name = EXCHANGES[2]['name']
    count = Trades.objects.count()
    record, response = save_trades(api=api, pair=pair, name=name, unixtime=unixtime)
    assert type(response) == list
    assert record.exchange == name
    assert record.unixtime == unixtime
    assert record.pair == pair[0]
    assert record.content == response
    assert Trades.objects.count() == count+1
