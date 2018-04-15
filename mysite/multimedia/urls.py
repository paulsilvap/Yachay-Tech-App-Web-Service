from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.multimedia_list, name='json object'),
]