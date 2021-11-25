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


class Post(Subreddit):
    def __init__(self, subreddit_name: str, post_id: str = None, post_idx: int = None, climit=10):
        assert bool(post_id) is not bool(post_idx), "Pass either a post_id or a post_idx, but not both"
        assert isinstance(post_id, str) or isinstance(post_idx, int), "Wrong type passed"
        super().__init__(subreddit_name)
        # TODO Geschickter lösen, so dass subreddit name nicht mehrfach gepasst werden muss
        self.post = self._get_post_from_post_id(post_id) if post_id else self._get_post_from_post_idx(post_idx)
        self.comments_ids = self._get_comments_ids(climit)

    def __repr__(self):
        return self.post.selftext

    def _get_post_from_post_id(self, post_id):
        return self.reddit_instance.submission(post_id)

    def _get_post_from_post_idx(self, post_idx):
        return self._get_post_from_post_id(self.posts_ids[post_idx])

    def _get_comments_ids(self, climit):
        pass


class Comment(Post):
    pass
