from binance.client import Client
from datetime import datetime
from pandas import DataFrame as df
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_SECRET_KEY')
client = Client(api_key, api_secret)

dogebtc = client.get_klines(
    symbol='DOGEBTC', interval=Client.KLINE_INTERVAL_1HOUR)
renbtc = client.get_klines(
    symbol='RENBTC', interval=Client.KLINE_INTERVAL_1HOUR)
grtbtc = client.get_klines(
    symbol='GRTBTC', interval=Client.KLINE_INTERVAL_1HOUR)
adabtc = client.get_klines(
    symbol='ADABTC', interval=Client.KLINE_INTERVAL_1HOUR)
btceur = client.get_klines(
    symbol='BTCEUR', interval=Client.KLINE_INTERVAL_1HOUR)
etheur = client.get_klines(
    symbol='ETHEUR', interval=Client.KLINE_INTERVAL_1HOUR)

print(btceur)
