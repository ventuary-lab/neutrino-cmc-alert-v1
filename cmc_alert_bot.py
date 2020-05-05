from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
import time
import config as cfg

def check_latest_quote(url, parameters, chat_id, minutes_between_checks, price_limit=0.985):
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        quote = data.get("data").get("5068").get("quote").get("USD")

        price = round(float(quote.get("price")),6)
        if price < price_limit:
            volume_24h = round(float(quote.get("volume_24h")),6)
            percent_change_1h = quote.get("percent_change_1h")
            percent_change_24h = quote.get("percent_change_24h")
            percent_change_7d = quote.get("percent_change_7d")
            market_cap = round(float(quote.get("market_cap")),6)
            last_updated = quote.get("last_updated")

            alert = '[...] WARNING: Current USDN price on CMC is less than $1 by more than 1.5%!\n\n'
            alert += f'Price: ${price}\n\n'
            alert += f'Other info:\n'
            alert += f'24h Volume: ${volume_24h}\n'
            alert += f'1h Price Change: {percent_change_1h}%\n'
            alert += f'24h Price Change: {percent_change_24h}%\n'
            alert += f'7d Price Change: {percent_change_7d}%\n'
            alert += f'Market Cap: ${market_cap}\n'
            alert += f'Last Updated: {last_updated}\n\n'
            alert += f'https://coinmarketcap.com/currencies/neutrino-dollar/\n\n'
            alert += f'Next check is due in {int(minutes_between_checks)} minutes\n\n'
            print(alert)
            send_alert_to_tg(alert, chat_id)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def send_alert_to_tg(alert, chat_id):
    try:
        bot_api_key = cfg.bot_api_key
        DATA = {"chat_id": chat_id, "text": alert}
        session.post(url="https://api.telegram.org/bot%s/sendMessage" % (bot_api_key), data=DATA)
        print("Sent alert to tg...")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    session = Session()
    session.headers.update(cfg.headers)

    send_alert_to_tg("[...] MESSAGE: Bot has restarted.",cfg.chat_id)

    status_update_counter = cfg.status_update_max

    while True:
        check_latest_quote(cfg.cmc_url, cfg.parameters, cfg.chat_id, cfg.seconds_between_checks/60, cfg.price_limit)
        status_update_counter -= 1
        if status_update_counter <= 0:
            send_alert_to_tg(
                "[...] MESSAGE: " + str(cfg.status_update_max) + " checks have passed. Bot is operating normally.",
                cfg.chat_id)
            status_update_counter = cfg.status_update_max
        time.sleep(cfg.seconds_between_checks)
