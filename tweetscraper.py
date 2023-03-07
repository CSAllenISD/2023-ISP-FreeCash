"""This file prints recent tweets with a certain stock ticker using Tweepy"""
import tweepy

#Number of Tweets to be pulled. Only 500,000 can be pulled per month.
max_results = 10
#Enter Twitter API keys
BEARER_TOKEN = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# You can authenticate as your app with just your bearer token

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

public_tweets = client.search_recent_tweets(query = "AAPL", tweet_fields=['created_at'], max_results=max_results)
tweets_list = public_tweets[0]
for tweet in tweets_list:
    with open('tweets.txt', 'a') as f:
        f.write(tweet.text + '\n')
        f.write(str(tweet.created_at) + '\n')
        f.write("========-========-========-========-========-========-========-========-\n")
        f.close()
        