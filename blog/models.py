from django.db import models

# Create your models here.

class MyPost(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    timestamp = models.DateTimeField()


    def __str__(self):
        return self.title