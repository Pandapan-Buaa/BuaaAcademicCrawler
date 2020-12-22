from django.conf.urls import url
from user import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from django.urls import include

urlpatterns = [
    url(r'^register/$', views.UserRegister.as_view()),
    # jwt认证模式
    url(r'^login/$', obtain_jwt_token),
    url(r'^info/$', views.UserInfo.as_view())
]
