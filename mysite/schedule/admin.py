from django.contrib import admin
from .models import Schedule

# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    fields = ['name','subject','time','day']
    list_display = ('name', 'subject', 'time', 'day')

admin.site.register(Schedule, ScheduleAdmin)