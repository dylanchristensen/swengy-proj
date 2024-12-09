from django.db import models
from django.contrib.auth.models import AbstractUser


class Track(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    track = models.ForeignKey(Track, null=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username']


class Path(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='paths')

    def __str__(self):
        return self.name


class Video(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.title


class Resource(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    content_url = models.URLField()

    def __str__(self):
        return self.title


class Project(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
