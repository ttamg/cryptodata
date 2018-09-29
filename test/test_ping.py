import time

from config import EXCHANGES
from cryptodata.save_ticker import save_ticker


"Unixtime set so that this can be deleted easily"
unixtime = 100.0


def test_ping_exchanges():
    """
    Test that we get responses from the exchanges
    :return:
    """

    for exch in EXCHANGES:
        assert exch['api'].get_markets()
        time.sleep(1)


def test_exchanges_and_pairs():
    """
    Test that ticker can be found for all exchanges and pairs
    :return:
    """
    for exch in EXCHANGES:
        api = exch['api']
        for pair in exch['pairs']:
            name = exch['name']
            record, response = save_ticker(api=api, pair=pair, name=name, unixtime=unixtime)
            time.sleep(1)
