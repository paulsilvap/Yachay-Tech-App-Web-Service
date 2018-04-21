from django.contrib import admin
from .models import Stop

# Register your models here.

class StopAdmin(admin.ModelAdmin):
    fields = ['route','stops']
    list_display = ('route', 'stops')

admin.site.register(Stop, StopAdmin)