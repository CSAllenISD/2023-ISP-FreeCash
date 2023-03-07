"""This file finds recent tweets with a certain stock ticker and writes their text and creation dates to a file"""
import tweepy
from dotenv import load_dotenv
load_dotenv()
import os

#Get variables from environment (from .env)
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

#Number of Tweets to be pulled. Only 500,000 can be pulled per month.
max_results = 10

#The following are environment variables stored in env.local, which should be in .gitignore
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
        