import configparser
import praw
import time

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config['reddit']['client_id']
client_secret = config['reddit']['client_secret']
user_agent = config['reddit']['user_agent']

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

subreddit = reddit.subreddit("wallstreetbets")
results = []

try:
    for submission in subreddit.search("$AAPL", sort="new", limit=10):
        result = {
            'title': submission.title,
            'url': submission.url
        }
        results.append(result)
        
except praw.exceptions.APIException as e:
    print(f"Encountered an error: {e}")
    print("Waiting for 60 seconds before retrying...")
    time.sleep(60)

for result in results:
    print(result['title'])
    print(result['url'])
    print("--------------------")
