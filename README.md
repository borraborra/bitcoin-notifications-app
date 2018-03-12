## Bitcoin Price Change Notifications Application

A Python application that sends a notification on the price of Bitcoin based on a tutorial published on [realpython.com](https://realpython.com/blog/python/python-bitcoin-ifttt/?__s=iyvx2pojonk7evuo5jrn). 

## How it works
The application makes use of  HTTP requests and sends them using the Python `requests` package. 

It also makes use of webhooks and connects them to external services, i.e., phone notifications and Telegram messages, by using the IFTTT ("if this, then that") web service that bridges the gap between different apps and devices.

```markdown
get_latest_bitcoin_price()
```

Gets and returns the Bitcoin price from [Coinmarketcap.com](coinmarketcap.com)

```markdown
post_ifttt_webhook(event, value)
```

Defines the payload send to IFTTT service, which is a POST request to the webhook URL.

```markdown
format_bitcoin_history(bitcoin_history)
```

Formats the date of retrieval into a string: 'day.month.year hour:minutes'. It also reformats price logs after 5 entries.
