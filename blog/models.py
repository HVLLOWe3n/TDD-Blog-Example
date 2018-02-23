from django.db import models
from datetime import datetime


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=datetime.now)
    # published_date = models.DateTimeField(default=datetime.now)

    # def publish(self):
      # self.published_date = datetime.now()

    def __str__(self):
        return self.title
