import reddit
from processor import Processor

def main():
    # Interaction with API
    subreddit = reddit.Subreddit("UnitBotTesting")
    for post_id in subreddit.posts_ids:
        post = reddit.Post(post_id)


if __name__ == "__main__":
    main()
