class Post:
    def __init__(self, content, user, timestamp):
        self.content = content
        self.user = user
        self.timestamp = timestamp
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)


class Comment:
    def __init__(self, content, user, timestamp):
        self.content = content
        self.user = user
        self.timestamp = timestamp


class SocialMediaFeed:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)


# Create a social media feed
feed = SocialMediaFeed()

# Add posts
post1 = Post("Hello world!", "User1", "2024-02-12 10:00:00")
post2 = Post("Python is awesome!", "User2", "2024-02-12 11:00:00")

feed.add_post(post1)
feed.add_post(post2)

# Add comments
post1.add_comment(Comment("Nice post!", "User3", "2024-02-12 10:05:00"))
post1.add_comment(Comment("Keep it up!", "User4", "2024-02-12 10:10:00"))


# Display posts and comments
for post in feed.posts:
    print(f"Post by {post.user} at {post.timestamp}: {post.content}")
    for comment in post.comments:
        print(f"  Comment by {comment.user} at {comment.timestamp}: {comment.content}")
