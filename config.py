seconds_between_checks = 55*60
status_update_max = 20

cmc_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'id':'5068' #USDN CMC id
}

chat_ids = {
    'test_channel':'', #fill with test channel id
    'cmc_warning_channel':'' #fill with cmc warning channel id
}

chat_id = chat_ids.get('test_channel') # warning Channel

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '', #fill with CMC pro api key
}

price_limit = 0.985

bot_api_key = "" #fill with TG bot api token