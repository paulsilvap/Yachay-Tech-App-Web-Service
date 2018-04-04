import datetime

from django.db import models
from django.utils import timezone
from polls.models import Question

#  Create your models here.
class New(models.Model):
    title = models.CharField(max_length=200)
    #dont forget use the max length
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    def __str__(self):
        return self.description
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        ordering = ('pub_date',)