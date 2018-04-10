import datetime

from django.db import models
from django.utils import timezone
from polls.models import Question

#  Create your models here.
class New(models.Model):
    title = models.CharField(max_length=200)
<<<<<<< HEAD
    image = models.ImageField()
=======
    #dont forget use the max length
>>>>>>> f72f869b9775e413da8be6c1cec64d2aa96c0037
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    def __str__(self):
        return self.description
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __file__(self):
        return self.image

    class Meta:
        ordering = ('pub_date',)