"""spartan_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^home/', views.home, name='home'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^search_list/', views.search_list, name='search_list'),
    url(r'^results/', views.results, name='results'),
    url(r'^review/', views.review, name='review'),
    url(r'^questionaire/', views.questionaire, name='questionaire'),
    url(r'^view_profile/', views.view_profile, name='view_profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
]
