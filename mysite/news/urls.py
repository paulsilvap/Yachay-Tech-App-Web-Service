from django.conf.urls import url, include
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register(r'news', views.NewViewSet)

#urlpatterns = [
#    url(r'^', include(router.urls)),
#]

urlpatterns = [
    url(r'^$', views.news_list, name='json object'),
]