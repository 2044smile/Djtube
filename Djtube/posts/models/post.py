from django.db import models
from users.models import User


class Post(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    video_id = models.CharField(
        max_length=16,
    )
    video_original_title = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    title = models.CharField(
        max_length=256,
    )
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_youtube_original_url(self):
        self.video_id='djtube'
        return "https://www.youtube.com/watch?v={post_video_id}".format(
            post_video_id=self.video_id
        )

    def __str__(self):
        return self.title
