import praw
import passwords as pwd

def main():
    reddit = praw.Reddit(
        client_id=pwd.reddit["client_id"],
        client_secret=pwd.reddit["client_secret"],
        user_agent="RedditUnitBot (by u/RedditUnitBot)",
    )


if __name__ == "__main__":
    main()