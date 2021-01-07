"""buaaac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'docs/', include_docs_urls(title="buaaac")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r"^admin/", admin.site.urls),
    #
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    path('api/user/', include('user.urls')),
    path('api/mongo/', include('mongo.urls')),
    path('api/crawler/', include('crawler.urls')),
]