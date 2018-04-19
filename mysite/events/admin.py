from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title','description']
    list_display = ('title', 'pub_date', 'description')

admin.site.register(Event, EventAdmin)