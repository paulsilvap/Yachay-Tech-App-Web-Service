from django.db import models
from django.utils import timezone
from . import myFields

# Create your models here.

class Time(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)

    # class Meta:
    #     db_table = 'schedule_time'

class Schedule(models.Model):
    DAYS_OF_THE_WEEK = (
        ('M','Monday'),
        ('TU','Tuesday'),
        ('W','Wednesday'),
        ('TH','Thursday'),
        ('F','Friday'),
        ('SA','Saturday'),
        ('SU','Sunday'),
    )
    day = models.CharField(max_length=2, choices=DAYS_OF_THE_WEEK)
    #day = myFields.DayOfTheWeekField()
    location = models.CharField(max_length=200)
    time = models.ForeignKey(Time)
 
    def __str__(self):
        return self.day
    def __str__(self):
        return self.location
    # def __str__(self):
    #     return str(self.time)

    # class Meta:
    #     ordering = ('day',)
        # db_table = 'schedule_schedule'

class Stop(models.Model):
    stop = models.CharField(max_length=200)

    def __str__(self):
        return self.stop

    # class Meta:
    #     db_table = 'schedule_stop'
    


