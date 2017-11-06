from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    creation_date = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/post/%d/' %self.pk

    class Meta:
        db_table = 'blog posts'
        ordering = ['-creation_date']