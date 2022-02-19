from django.conf import settings
from apps.base.models import BaseModel
from django.db import models

class Post(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()

    @property
    def post_str(self):
        return f"{self.author.username}: {self.content[0:15]}..." if len(self.content) > 15 else f"{self.content}"

    def __repr__(self):
        return self.post_str

    def __str__(self):
        return self.post_str


class PostLike(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    @property
    def post_like_str(self):
        post_str = f"{self.post.title[0:10]}..." if len(self.post.title) > 15 else f"{self.post.title}" + f" by {self.post.author.username}"
        return f"Like by {self.author.username} on post {post_str}"

    def __repr__(self):
        return self.post_like_str

    def __str__(self):
        return self.post_like_str


class PostComment(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    @property
    def post_comment_str(self):
        post_str = f"{self.post.title[0:10]}..." if len(self.post.title) > 15 else f"{self.post.title}" + f" by {self.post.author.username}"
        return f"Comment by {self.author.username} on post {post_str}"

    def __repr__(self):
        return self.post_comment_str

    def __str__(self):
        return self.post_comment_str


class CommentLike(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)

    @property
    def comment_like_str(self):
        comment_str = f"{self.comment.content[0:10]}..." if len(self.comment.content) > 15 else f"{self.comment.content}" + f" by {self.comment.author.username}"
        return f"Like by {self.author.username} on comment {comment_str}"

    def __repr__(self):
        return self.comment_like_str

    def __str__(self):
        return self.comment_like_str
