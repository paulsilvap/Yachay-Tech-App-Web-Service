from django.contrib import admin
from .models import Multimedia

# Register your models here.

class MultimediaAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title','description','archivo']
    list_display = ('title', 'pub_date', 'description','archivo')

admin.site.register(Multimedia, MultimediaAdmin)