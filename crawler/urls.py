from django.conf.urls import url
from crawler import views


urlpatterns = [
    url(r'^file/$', views.XpathFileList.as_view()),
]
