import datetime
import os
from django.db import models
from django.utils import timezone

#  Create your models here.
class New(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='news', default = 'null')
    pub_date = models.DateTimeField('date published')
    summary = models.CharField(max_length=300)
    description = models.TextField()
    objects = NewSearchListView()
    def __str__(self):
        return self.description
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.summary
    

    class Meta:
        ordering = ('pub_date',)

    