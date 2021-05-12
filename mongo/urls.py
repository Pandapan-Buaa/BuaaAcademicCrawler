from django.conf.urls import url
from mongo import views
from django.urls import include

urlpatterns = [
    url(r'^getAll/$', views.getAllInfo.as_view()),
    url(r'^getByName/$', views.getByName.as_view()),
    url(r'^getOrganization/$', views.getOrganizationName.as_view()),
    url(r'^getCollege/$', views.getCollegeName.as_view()),
    url(r'^getPerson/$', views.getPersonName.as_view()),
    url(r'^getPersonInfo/$', views.getPersonInfo.as_view()),
    url(r'^getZhituInfo/$', views.getZhituInfo.as_view()),
    url(r'^getZhituRelation/$', views.getZhituRelation.as_view()),
    url(r'^getUrl/$', views.getUrlByName.as_view()),
    url(r'^exportCsv/$', views.exportAsCSV.as_view()),
    url(r'^getZhituOrgInfo/$', views.getZhituOrgInfo.as_view()),
]


