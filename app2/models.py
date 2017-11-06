from django.db import models

# Create your models here.
class Reliz(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    pub_date = models.DateTimeField()
    avtor = models.CharField(max_length=120)


    class Meta:
        get_latest_by = 'pub_date'

    def get_absolute_url(self):
        return '/app2/%d' %self.id

    def __unicode__(self):
        return self.title