import praw

import passwords as pwd
from typing import Union


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
    def __init__(self, subreddit_name: str, plimit: int = 1000):
        super().__init__()
        self.subreddit_instance = self.reddit_instance.subreddit(subreddit_name)
        self.posts_ids = self._get_subreddit_posts_ids(plimit=plimit)

    def _get_subreddit_posts_ids(self, plimit):
        subreddit = self.subreddit_instance.hot(limit=plimit)
        return [post.id for post in subreddit]
        # TODO also implement for other reddit sorting methods (new, rising etc)
        # TODO make abstract method (since also usable on comments?)


class Post(RedditInstance):
    def __init__(self, post_id: str):
        assert isinstance(post_id, str), "The parameter post_id must be passed as type string."
        super().__init__()
        self.post = self._get_post(post_id)
        self.comments_ids = self._get_comments_ids(self.post)

    def __repr__(self):
        title_body_boundary = len(self.post.title) * "-"
        posts_boundary = 2 * f"{40 * '-'}\n"
        return f"{self.post.title}\n{title_body_boundary}\n{self.post.selftext}\n{posts_boundary}\n\n"

    def _get_post(self, post_id):
        return self.reddit_instance.submission(post_id)

    def _get_comments_ids(self, cparent):
        return [comment.id for comment in cparent.comments]


class Comment(RedditInstance):
    def __init__(self, comment_id: str):
        assert isinstance(comment_id, str), "The parameter comment_id must be passed as type string."
        super().__init__()
        self.comment = self.reddit_instance.comment(comment_id)
        self.comments_ids = self._get_comments_ids()

    def __repr__(self):
        return self.comment.body

    def _get_comments_ids(self):
        self.comment.refresh()  # see https://github.com/praw-dev/praw/issues/413
        return [comment.id for comment in self.comment.replies]

    #TODO flatten comment tree
