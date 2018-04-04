from django.contrib import admin

from .models import File

class NewAdmin(admin.ModelAdmin):
    fields = ['name', 'pub_date','image_description']
    list_display = ('name', 'pub_date', 'image_description')

admin.site.register(File, NewAdmin)
