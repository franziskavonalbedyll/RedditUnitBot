import praw
import praw.models
import prawcore

import helpers
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
            username=pwd.reddit["user"],
            password=pwd.reddit["pwd"]
        )

    def comment_converted_units(self, replying_to_id, reply: str):
        self.reddit_instance.submission(id=replying_to_id).reply(reply)
        try:
            self.reddit_instance.submission(id=replying_to_id).reply(reply)
        except prawcore.exceptions.Forbidden:
            self.reddit_instance.comment(id=replying_to_id).reply(reply)


class Subreddit(RedditInstance):
    def __init__(self, subreddit_name: str, plimit: int = 1000):
        super().__init__()
        self.subreddit_instance = self.reddit_instance.subreddit(subreddit_name)
        self.posts_ids = self._get_subreddit_posts_ids(plimit=plimit)

    def __len__(self):
        return len(self.posts_ids)

    def _get_subreddit_posts_ids(self, plimit):
        subreddit = self.subreddit_instance.hot(limit=plimit)
        return [post.id for post in subreddit]
        # TODO also implement for other reddit sorting methods (new, rising etc)


class Post(RedditInstance):
    def __init__(self, post_id: str):
        assert isinstance(post_id, str), "The parameter post_id must be passed as type string."
        super().__init__()
        self.post_id = post_id
        self.post = self._get_post(post_id)
        self.comments_ids = FlattenedCommentTree(self.post)

    def __repr__(self):
        title_body_boundary = len(self.post.title) * "-"
        body_comments_boundary = len(self.post.title) * "."
        post_post_boundary = 2 * f"{40 * '-'}\n"
        return f"{self.post.title}\n{title_body_boundary}\n{self.post.selftext}\n{body_comments_boundary}\n{repr(self.comments_ids)}\n{post_post_boundary}"

    def _get_post(self, post_id):
        return self.reddit_instance.submission(post_id)

    def _get_comments_ids(self, cparent):
        return [comment.id for comment in cparent.comments]


class FlattenedCommentTree:
    def __init__(self, post: Post):
        self.flattened_comment_tree = self._flatten_comment_tree(post.comments)
        self.comments_ids = [comment.id for comment in self.flattened_comment_tree]

    def __repr__(self):
        return "".join([f"{Comment(comment_id)}\n" for comment_id in self.comments_ids])

    def _flatten_comment_tree(self, cf: praw.models.comment_forest.CommentForest):
        if isinstance(cf, praw.models.comment_forest.CommentForest) and len(cf._comments) != 0:
            return helpers.flatten_multi_nested_list([self._flatten_comment_tree(id) for id in cf])
        elif isinstance(cf, praw.models.Comment) and len(cf.replies) != 0:
            return [cf] + [self._flatten_comment_tree(sub_id) for sub_id in cf.replies]
        else:
            return cf


class Comment(RedditInstance):
    def __init__(self, comment_id: str):
        assert isinstance(comment_id, str), "The parameter comment_id must be passed as type string."
        super().__init__()
        self.comment = self.reddit_instance.comment(comment_id)

    def __repr__(self):
        return self.comment.body
