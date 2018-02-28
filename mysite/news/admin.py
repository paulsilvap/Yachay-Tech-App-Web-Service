from django.contrib import admin
from .models import New

# Register your models here.

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# admin.site.register(Question, QuestionAdmin)

class NewAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title','description']
    list_display = ('title', 'pub_date', 'description')

admin.site.register(New, NewAdmin)