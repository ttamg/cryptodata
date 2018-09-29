from cryptotik import PoloniexNormalized
from cryptotik import BittrexNormalized
from cryptotik import HitbtcNormalized
from cryptotik import BitstampNormalized
from cryptotik import BinanceNormalized


# Period in seconds between restarting the job
PERIOD = 60

# Name of MongoDB database to use or create (if not already existing)
DATABASE = 'btcusd_1minute'

# Exchange apis to use and pairs (a tuple with common name and cryptotik pair name)
EXCHANGES = [
    {
        'api': PoloniexNormalized(),
        'name': 'Poloniex',
        'pairs': [
            ('btc-usd', 'btc-usdt'),
        ]
    },
    {
        'api': BittrexNormalized(),
        'name': 'Bittrex',
        'pairs': [
            ('btc-usd', 'btc-usdt'),
        ]
    },
    {
        'api': BinanceNormalized(),
        'name': 'Binance',
        'pairs': [
            ('btc-usd', 'btc-usdt'),
        ]
    },
    {
        'api': HitbtcNormalized(),
        'name': 'HitBTC',
        'pairs': [
            ('btc-usd', 'btc-usd'),
        ]
    },
    {
        'api': BitstampNormalized(),
        'name': 'Bitstamp',
        'pairs': [
            ('btc-usd', 'btc-usd'),
        ]
    },
    # {
    #     'api': KrakenNormalized(),
    #     'name': 'Kraken',
    #     'pairs': [
    #         ('btc-usd', 'xbt-usd'),
    #     ]
    # },
    # {
    #     'api': Bitmex(),
    #     'name': 'Bitmex',
    #     'pairs': [
    #         ('btc-usd', 'XBTUSD'),
    #     ]
    # },
    # OKEX,
    # BIthumb,
    # Bitfinex,
]
