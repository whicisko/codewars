def generate_hashtag(s):
    return False if len(s) > 140 or len(s) <= 0 else "#" + s.title().replace(" ", "")
