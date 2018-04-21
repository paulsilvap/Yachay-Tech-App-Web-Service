from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.schedule_list, name='json object'),
]