# neutrino-cmc-alert

## How to run

1. Register and receive a free CMC api token: https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest
2. Create a telegram bot and obtain its api token: https://core.telegram.org/bots#creating-a-new-bot
3. Get telegram channel ids: https://gist.github.com/mraaroncruz/e76d19f7d61d59419002db54030ebe35
4. Fill the above information into the ```config.py```
5. ```pip install -r requirements.txt```
6. To run: ```python3 cmc_alert_bot.py```
