def check_if_comment_already_processed(comment):
    return True if comment.id in PROCESSED_COMMENTS_IDS else False


def search_for_mentions_of_unit(unit: str, comment):
    return True if unit in comment.body else False
