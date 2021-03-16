import requests
import pandas as pd

def conversion_currency(currency):
    url = 'https://v6.exchangerate-api.com/v6/7ee0700616ce0cb7e8eb996d/latest/' + currency
    response = requests.get(url)
    data = response.json()
    
    return data
    