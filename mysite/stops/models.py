from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Stop(models.Model):
    route = models.CharField(max_length=200)
    stops = ArrayField(
        models.CharField (max_length=200),
        size=20,
        )
    def __str__(self):
        return self.route

    class Meta:
        ordering = ('route',)