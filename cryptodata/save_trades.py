from mongo.mongo import Trades

from cryptodata.logger import log
log.debug(f'Loading module {__name__}')


def save_trades(api, pair, name, unixtime):
    """
    Fetches and records the recent trades on the exchange and pair
    :param api: Exchange API
    :param pair: Tuple of strings for pairs
    :return: None
    """
    try:
        response = api.get_market_trade_history(pair[1])
    except:
        raise Exception(f'Failed to get trade history on exchange {name} and pair {pair[1]}')

    record = Trades(
        unixtime=unixtime,
        exchange=name,
        pair=pair[0],
        content=response,
    )
    record.save()

    log.debug(f'Saved trade history record on {name} and {pair}')
    return record, response
