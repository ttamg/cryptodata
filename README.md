# cryptodata
A simple bot that will continuously harvest market data from exchanges and store the responses in a MongoDB database.


## Purpose

Market data on cryptocurrencies is readily available from exchanges via
REST APIs and some websites. But it tends to be limited to just a few thousand rows of data
or recent history only. 

If you want to train machine-learning models or neural nets, particularly if we are using 
many features, we need a lot more data than this.  

This bot is a way to start to build your own database of market data that you can then
query and mine to create datasets for analytics and machine learning.


## Installation

Clone or fork this GitHub repository.

Create a virtual environment with Python 3.6 or later - [this post may be helpful](https://medium.com/the-python-corner/using-virtual-environments-with-python-7166d3bfa218) 

Install the required packages within that virtual environment - From the cryptodata project directory run:

    pip install -r requirements.txt
    
Install MongoDB and ensure the mongod server is running - [see the official docs](https://docs.mongodb.com/guides/server/install/)

This bot uses the [**cryptotik**](https://github.com/indiciumfund/cryptotik) library to standardise
the API calls to the cryptocurrency exchanges.


## Configuration

All the configuartion options are contained in the **config.py* file


### Database

**DATABASE** should be the name of your MongoDB database - this will add to an existing database or 
create a new one


### Periodicity

**PERIOD** is set in the number of sections between each snapshot of data to be taken.
e.g. PERIOD=60 for capturing data every minute.

*Warning* - be aware that most exchanges impose rate limits and will block your API calls or even ban your IP 
address if you hit the exchange with too many API calls in too short a period.  You are responsible for not
collecting data for too many pairs too often.


### Exchanges and pairs

**EXCHANGES** sets the exchanges and pairs to include in the data harvesting routines.
**EXCHANGES** is a list of dictionaries, one for each exchange:

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
    ]
    
*api* is the *cryptotik public api* for the exchange.

*name* is a string name of the exchange

*pairs* is a list of 2-tuples of pairs to include in the bot activity. The first item in 
each tuple is the common name for the pair to store in the database. The second item in the tuple is
the pair name that **cryptotik* requires for that exchange


## Running the bot

Start the bot by running the **cryptodata.py** module.

    python cryptodata.py

This module wakes the bot every period, creates a new thread for each 
combination of exchange and pair to be fetched, and starts all threads. 
Each individual thread fetches the market data via the exchange API and stores the 
response in the database


## Tests

Simple unit tests have been written. To check your installation you can run **pytest** from the 
main cryptodata directory.


## Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


## Issues and improvements

Known issues as at October 2018 (v0.1):

*   Not all **cryptotik** exchanges have all the methods written and therefore are not yet
    possible to use in the bot. e.g. BitMex
    
    
## Feedback

If you find this useful, please give it a star.

If you are developer and see an improvement, please feel free to fork and make improvements. 
Pull requests are welcomed.

