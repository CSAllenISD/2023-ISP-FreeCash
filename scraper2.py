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

auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
api = tweepy.API(auth)

public_tweets = client.search_recent_tweets(query = "lovs", tweet_fields=['created_at'], max_results=max_results)
tweets_list = public_tweets[0]
for tweet in tweets_list:
    with open('tweets.txt', 'a') as f:
        f.write(tweet.text + '\n')
        f.write(str(tweet.created_at) + '\n')
        f.write("========-========-========-========-========-========-========-========-\n")
        f.close()
        