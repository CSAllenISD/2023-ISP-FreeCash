import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample text to analyze
text = "I love this product! It's amazing."

# Use the sentiment analyzer to determine sentiment scores
scores = sia.polarity_scores(text)

# Print the sentiment scores
print(scores)

# Determine the sentiment based on the polarity score
if scores['compound'] > 0:
    print("Positive sentiment")
elif scores['compound'] < 0:
    print("Negative sentiment")
else:
    print("Neutral sentiment")
