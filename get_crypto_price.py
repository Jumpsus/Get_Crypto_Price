# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 20:56:50 2021

@author: Jumpsus
"""

import urllib.request as ur
import json

url_index = 'https://api.coingecko.com/api/v3/coins/list' #api from coingecko
read = ur.urlopen(url_index).read() #request data from web inthis process you need to connect internet
index = json.loads(read)

currency = input("Currency (US Dollar = usd, Thai Baht = thb):")
currency = currency.lower()

try:
    while True:
        ids = input("Put Crypto Currency Symbol (btc, eth, sol etc...):")
        ids = ids.lower()
        ticker = False
        for x in index:
            if(ids == x['symbol']):
                url = 'https://api.coingecko.com/api/v3/simple/price?ids='+ x['id'] + '&vs_currencies=' + currency
                read = ur.urlopen(url).read()
                data = json.loads(read)
                result = data[x['id']][currency]
                print("{0} {1}".format(data[x['id']][currency],currency))
                ticker = True
                break
        if (not ticker):
            print("Fail: Please Check Symbol Again !!")
        pass
        
except KeyboardInterrupt:
    print("Closed")
    pass
