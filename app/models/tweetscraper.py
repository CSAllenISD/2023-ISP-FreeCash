"""This file finds recent tweets with a certain stock ticker and writes their text and creation dates to a file"""
import tweepy
from dotenv import load_dotenv
load_dotenv()
import os

#Every hour from 1:30-2:30PM to 6:30-7:30PM, while the stock market is open
hour_ranges = [["13:30:00", "14:30:00"], 
               ["14:30:00", "15:30:00"], 
               ["15:30:00", "16:30:00"], 
               ["16:30:00", "17:30:00"], 
               ["17:30:00", "18:30:00"], 
               ["18:30:00", "19:30:00"]]

#Update to most recent 7 days or most recent 7 days excluding today
days = ["2023-03-24", 
        "2023-03-25", 
        "2023-03-26", 
        "2023-03-27", 
        "2023-03-28", 
        "2023-03-29"]

queries = ["AAPL", "GOOG"]

#Get variables from environment (from .env)
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

#Number of Tweets to be pulled. Only 500,000 can be pulled per month.
max_results = 10

#The following are environment variables stored in .env, which should be in .gitignore
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

timestamps = []
for day in days:
    for hour_range in hour_ranges:
        start_time = hour_range[0]
        end_time = hour_range[1]
        timestamp_start = day + "T" + start_time + "Z"
        timestamp_end = day + "T" + end_time + "Z"
        timestamp = [timestamp_start, timestamp_end]
        timestamps.append(timestamp)

for query in queries:
    for timestamp in timestamps:
        public_tweets = client.search_recent_tweets(query = query, tweet_fields=['created_at'], max_results=max_results, start_time=timestamp[0], end_time=timestamp[1])
        tweets_list = public_tweets[0]
        with open('tweets.txt', 'a') as f:
            for tweet in tweets_list:
                f.write(tweet.text + '\n')
                f.write(str(tweet.created_at) + '\n')
                f.write("========-========-========-========-========-========-========-========-\n")
            f.close()
