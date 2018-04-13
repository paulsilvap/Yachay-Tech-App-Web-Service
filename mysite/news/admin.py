from django.contrib import admin
from .models import New

class NewAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title','summary','description','image']
    list_display = ('title', 'pub_date','summary', 'description','image')

admin.site.register(New, NewAdmin)