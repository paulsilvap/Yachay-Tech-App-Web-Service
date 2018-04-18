from django.contrib import admin
from .models import Time, Stop, Schedule

# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    fields = ['day','location','time']
    list_display = ('day', 'location', 'time')

class StopAdmin(admin.ModelAdmin):
    fields = ['location','stop']
    list_display = ('location','stop')

class TimeAdmin(admin.ModelAdmin):
    fields = ['time']
    list_display = ('time',)

admin.site.register(Schedule, ScheduleAdmin,)
admin.site.register(Stop, StopAdmin)
admin.site.register(Time, TimeAdmin)