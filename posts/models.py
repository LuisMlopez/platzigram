from django.db import models
from django.contrib.auth.models import User

from users.models import Profile


class Post(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{title} by @{username}'.format(
            title=self.title,
            username=self.user.username
        )
