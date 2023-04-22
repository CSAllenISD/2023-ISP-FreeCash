import json
from textblob import TextBlob

def find_most_positive_sentiment(tweet_json):
    # Load the tweet data from the JSON string
    tweet_data = json.loads(tweet_json)
    
    # Create a list to store the sentiment polarity scores
    sentiment_scores = []
    
    # Loop through each tweet and get the sentiment polarity score
    for tweet in tweet_data:
        text = tweet["text"]
        sentiment = TextBlob(text).sentiment.polarity
        sentiment_scores.append(sentiment)
    
    # Get the index of the maximum value in the list of sentiment scores
    max_index = sentiment_scores.index(max(sentiment_scores))
    
    # Return the index
    return max_index
