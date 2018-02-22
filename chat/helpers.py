import urllib.request as ur
import json
import time


def get_curse():
    link = 'https://api.coinmarketcap.com/v1/ticker'
    byte_json = ur.urlopen(link)
    cache_curse = json.loads(byte_json.read().decode())
    res_cache = {}
    for i in cache_curse:
        res_cache[i['symbol']] = i['price_usd']

    res_cache['time'] = time.time()
    return res_cache
