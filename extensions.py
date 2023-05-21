import requests
import json
from config import keys

class APIExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote, base, amount):

        if quote==base:
            raise APIExeption(f'Невозможно перевести одинаковые валюты: {base}!')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту: {quote}!')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту: {base}!')
        
        try:
            amount = float(amount)
        except:
            raise APIExeption(f'Не удалось обработать количество: {amount}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        return f'Цена {amount} {quote} в {base} - {round(float(json.loads(r.content)[keys[base]])*amount,2)}'
