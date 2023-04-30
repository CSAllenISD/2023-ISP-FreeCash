import json
from textblob import TextBlob

def find_most_positive_sentiment(tweet_json):
    try:
        # Load the tweet data from the JSON string
        tweet_data = json.loads(tweet_json)

        # Create a list to store the sentiment polarity scores
        sentiment_scores = []

        # Loop through each tweet and get the sentiment polarity score using list comprehension
        sentiment_scores = [TextBlob(tweet["text"]).sentiment.polarity for tweet in tweet_data]

        # Get the index of the maximum value in the list of sentiment scores
        max_index = sentiment_scores.index(max(sentiment_scores))

        # Return the index
        return max_index

    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        return None
