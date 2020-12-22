from django.conf.urls import url
from mongo import views
from django.urls import include

urlpatterns = [
    url(r'^getall/$', views.GetAllInfo.as_view()),
    url(r'^getbyname/$', views.GetByName.as_view()),
]
