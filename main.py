import reddit


def main():
    subreddit = reddit.Subreddit("UnitBotTesting")
    for post_id in subreddit.posts_ids:
        post = reddit.Post(post_id)
        print(post)


if __name__ == "__main__":
    main()
