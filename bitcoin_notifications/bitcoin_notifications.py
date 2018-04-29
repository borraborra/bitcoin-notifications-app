# -*- coding: utf-8 -*-

# We want to get the latest price from the Coinmarketcap API.

# The usual suspects ...
import requests
import time
from datetime import datetime

BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/bitcoin_emergency_alert/with/key/mykey'

def get_latest_bitcoin_price():
    response, response_json = requests.get(BITCOIN_API_URL), response.json()
    # Convert the price to a floating point number
    return float(response_json[0]['price_usd'])

def post_ifttt_webhook(event, value):
    # The payload that will be sent to IFTTT service
    data = {'value1': value}
    # Inserts our desired event
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    # Sends a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, json=data)

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        # Formats the date into a string: 'day.month.year hour:minutes'
        date, price = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M'), bitcoin_price['price']
        # <b> (bold) tag creates bolded text
        # 24.02.2018 15:09: $<b>10123.4</b>
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)
    # Use a <br> (break) tag to create a new line.
    # Join the rows delimited by <br> tag: row1<br>row2<br>row3
    return '<br>'.join(rows)

BITCOIN_PRICE_THRESHOLD = 10000

def main():
    bitcoin_history = []
    while True:
        price, date = get_latest_bitcoin_price(), datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_emergency_alert', price)
        # Send a Telegram notification.
        # Once we have 5 items in our bitcoin_history, send an update.
        if (len(bitcoin_history) == 5):
            post_ifttt_webhook('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            # Reset the history
            bitcoin_history = []
        # Sleet for 5 minutes
        time.sleep(5 * 60)

if __name__ == '__main__':
    main()
