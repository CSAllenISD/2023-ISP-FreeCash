"""This file prints recent tweets with a certain stock ticker using Tweepy"""
import tweepy

#Number of Tweets to be pulled. Only 500,000 can be pulled per month.
max_results = 10
#Enter Twitter API keys
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACK0lgEAAAAAwbhuEpAJPc%2FzvtA4GfgDVAQ0pM4%3'\
    'Dn8noDHkYdSq68Gb5w6K9vSHFIYPWIGwpYe5aW8YjqxBtWSIvCS'
CONSUMER_KEY = "8v37VAM8vNdTPnryGHknPYxPB"
CONSUMER_SECRET = "VDBqLpbCmNMgJlfccIhESW3SQV65gTozXptLdEOswMWPz2RR1P"
ACCESS_TOKEN = "1622677068256272385-gclBcFkJPllp0MS8lRiB6k7vlXNTNR"
ACCESS_TOKEN_SECRET = "bGsN6ZyuxvNqHNNzshOFbsjNB4E6PY6zyXUWCeQHlawLa"

# You can authenticate as your app with just your bearer token

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

public_tweets = client.search_recent_tweets(query = "AAPL", tweet_fields=['created_at'], max_results=max_results)
print(type(public_tweets))
tweets_list = public_tweets[0]
print(type(tweets_list))
for tweet in tweets_list:
    print(tweet.text)
    print(tweet.created_at)
    print("-----------------------------------------------------------------------------")
    
#with open("foo.txt", "a") as f:
 #    f.write("new line\n")