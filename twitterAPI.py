import tweepy

#Enter Twitter API keys
bearer_token = "AAAAAAAAAAAAAAAAAAAAACK0lgEAAAAAwbhuEpAJPc%2FzvtA4GfgDVAQ0pM4%3Dn8noDHkYdSq68Gb5w6K9vSHFIYPWIGwpYe5aW8YjqxBtWSIvCS"
consumer_key = "8v37VAM8vNdTPnryGHknPYxPB"
consumer_secret = "VDBqLpbCmNMgJlfccIhESW3SQV65gTozXptLdEOswMWPz2RR1P"
access_token = "1622677068256272385-gclBcFkJPllp0MS8lRiB6k7vlXNTNR"
access_token_secret = "bGsN6ZyuxvNqHNNzshOFbsjNB4E6PY6zyXUWCeQHlawLa"

# You can authenticate as your app with just your bearer token

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret,
    bearer_token=bearer_token
)

public_tweets = client.search_recent_tweets("AAPL")
print(public_tweets)