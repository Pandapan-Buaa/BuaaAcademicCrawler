from django.conf.urls import url
from mongo import views
from django.urls import include

urlpatterns = [
    url(r'^getAll/$', views.getAllInfo.as_view()),
    url(r'^getByName/$', views.getByName.as_view()),
    url(r'^getOrganization/$', views.getOrganizationName.as_view()),
    url(r'^getCollege/$', views.getCollegeName.as_view()),
    url(r'^getUrl/$', views.getUrlByName.as_view()),
]
