import praw

reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="your_user_agent",
)

subreddit = reddit.subreddit("wallstreetbets")

for submission in subreddit.search("$AAPL", sort="new", limit=10):
    print(submission.title)
    print(submission.url)
    print("--------------------")
