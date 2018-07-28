from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.appmain, name='appmain'),
    url(r'^fifa$', views.appfifa, name='appfifa'),
    url(r'^flag$', views.appflag, name='appflag'),
]
