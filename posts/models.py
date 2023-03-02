from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="posts")
    date_added = models.DateTimeField(_("Date added"), default=timezone.now)

    def __str__(self):
        return f"{self.title!r} wrote by {self.user}"


class Like(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    date_added = models.DateTimeField(_("Date added"), default=timezone.now)

    def __str__(self):
        return f"Like made by {self.user} on {self.post}"
