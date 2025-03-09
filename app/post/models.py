from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "user.User",
        related_name="posts",
        on_delete=models.CASCADE)
    post_text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.publication_date}"


class Comment(models.Model):
    author = models.ForeignKey(
        "user.User",
        related_name="comments",
        on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        "Post",
        related_name="comments",
        on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}, {self.create_date}/n{self.comment_text}"
