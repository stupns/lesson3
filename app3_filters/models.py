from django.db import models


class MyFilters(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    pub_date = models.DateTimeField()
    avtor = models.CharField(max_length=120)

    def __unicode__(self):
        return self.avtor