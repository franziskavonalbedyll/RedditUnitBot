import praw

import passwords as pwd


class RedditInstance:
    def __init__(self):
        self.reddit_instance = RedditInstance.login()

    @staticmethod
    def login():
        return praw.Reddit(
            client_id=pwd.reddit["client_id"],
            client_secret=pwd.reddit["client_secret"],
            user_agent="RedditUnitBot (by u/RedditUnitBot)",
        )

    def comment_converted_units():
        pass


class Subreddit(RedditInstance):
    def __init__(self, subreddit_name: str, plimit: int = 1):
        super().__init__()
        self.subreddit_instance = self.reddit_instance.subreddit(subreddit_name)
        self.posts_ids = self._get_subreddit_posts_ids(plimit=plimit)

    def _get_subreddit_posts_ids(self, plimit):
        subreddit = self.subreddit_instance.hot(limit=plimit)
        return [post.id for post in subreddit]
        # TODO also implement for other reddit sorting methods (new, rising etc)
        # TODO make abstract method (since also usable on comments?)


class Post(RedditInstance):
    def __init__(self, post_id: str, climit=10):
        assert isinstance(post_id, str), "The parameter post_id must be passed as type string."
        super().__init__()
        self.post = self._get_post(post_id)
        self.comments_ids = self._get_comments_ids(climit)

    def __repr__(self):
        return self.post.selftext

    def _get_post(self, post_id):
        return self.reddit_instance.submission(post_id)

    def _get_comments_ids(self, climit):
        pass


class Comment(Post):
    pass
