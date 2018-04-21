import datetime
from django.db import models
from django.utils import timezone

class Multimedia(models.Model):
    title = models.CharField(max_length=200,help_text="Enter the title")
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    archivo= models.FileField(upload_to='multimedia')#cambio
    def __str__(self):
        return self.title
    def __str__(self):
        return self.description
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    class Meta:
        ordering = ('pub_date',)