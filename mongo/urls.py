from django.conf.urls import url
from mongo import views
from django.urls import include

urlpatterns = [
    url(r'^getAll/$', views.GetAllInfo.as_view()),
    url(r'^getByName/$', views.GetByName.as_view()),
    url(r'^getOrganization/$', views.GetOrganizationName.as_view()),
]
