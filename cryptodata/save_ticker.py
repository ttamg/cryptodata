from mongo.mongo import Ticker

from utils.logger import log
log.debug(f'Loading module {__name__}')


def save_ticker(api, pair, name, unixtime):
    """
    Fetches and records the market ticker for the exchange and pair
    :param api: Exchange API
    :param pair: Tuple of strings for pairs
    :return: None
    """
    try:
        response = api.get_market_ticker(pair[1])
    except:
        raise Exception(f'Failed to get ticker on exchange {name} and pair {pair[1]}')

    record = Ticker(
        unixtime=unixtime,
        exchange=name,
        pair=pair[0],
        content=response,
    )
    record.save()

    log.debug(f'Saved ticker record on {name} and {pair}')
    return record, response
