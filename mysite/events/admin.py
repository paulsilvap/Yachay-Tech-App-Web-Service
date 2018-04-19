from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title','description','image']
    list_display = ('title', 'pub_date', 'description','image')

admin.site.register(Event, EventAdmin)
