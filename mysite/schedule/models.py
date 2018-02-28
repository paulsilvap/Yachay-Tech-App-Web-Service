from django.db import models
from django.utils import timezone

# Create your models here.

class Schedule(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
 
    def __str__(self):
        return self.name
    def __str__(self):
        return self.subject
    def __str__(self):
        return self.time
    def __str__(self):
        return self.day

    class Meta:
        ordering = ('name',)