import time, datetime

from utils.scheduler import unixtime_period
from utils.threading import run_threaded
from config import EXCHANGES, PERIOD
from cryptodata.save_ticker import save_ticker
from cryptodata.save_orderbook import save_orderbook
from cryptodata.save_trades import save_trades

import logging
from utils.logger import log
log.debug(f'Loading module {__name__}')
log.setLevel(logging.INFO)


def master_job(unixtime=None):
    """
    Kicks off all the data collection and writing to the database
    :return:
    """
    log.info(f'Started master job at time {time.ctime()} and unixtime {unixtime}')

    if not unixtime:
        unixtime = datetime.datetime.now().timestamp()

    jobs = [save_orderbook, save_trades, save_ticker]
    for job in jobs:
        for exch in EXCHANGES:
            for pair in exch['pairs']:
                run_threaded(job, {
                    'api': exch['api'],
                    'pair': pair,
                    'name': exch['name'],
                    'unixtime': unixtime,
                })


def run_timer():
    """
    Main running programme - that waits until a specified number of seconds from the epoch and then runs the job
    :return:
    """

    unixtime = 0
    while True:
        new_unixtime = unixtime_period(PERIOD)
        if new_unixtime != unixtime:
            run_threaded(master_job, {'unixtime': new_unixtime})
            unixtime = new_unixtime

        time.sleep(0.5)


if __name__ == '__main__':
    run_timer()
