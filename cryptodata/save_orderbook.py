from mongo.mongo import Orderbook

from cryptodata.logger import log
log.debug(f'Loading module {__name__}')


def save_orderbook(api, pair, name, unixtime):
    """
    Fetches and records the orderbook on the exchange and pair
    :param api: Exchange API
    :param pair: Tuple of strings for pairs
    :return: None
    """
    try:
        response = api.get_market_orders(pair[1])
    except:
        raise Exception(f'Failed to get orderbook on exchange {name} and pair {pair[1]}')

    record = Orderbook(
        unixtime=unixtime,
        exchange=name,
        pair=pair[0],
        content=response,
    )
    record.save()

    log.debug(f'Saved orderbook record on {name} and {pair}')
    return record, response
