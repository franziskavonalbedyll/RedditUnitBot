import reddit
from processor import Processor

def main():
    # Interaction with API
    subreddit = reddit.Subreddit("UnitBotTesting")
    for post_id in subreddit.posts_ids:
        post = reddit.Post(post_id)
        xd = Processor.get_answer_text(post.body.selftext)
        if not xd: continue
        Processor



if __name__ == "__main__":
    main()
