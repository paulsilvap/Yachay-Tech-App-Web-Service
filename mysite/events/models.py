import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images', default = 'null')
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    def __str__(self):
        return self.title
    def __str__(self):
        return self.description
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        ordering = ('pub_date',)