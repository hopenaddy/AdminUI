from django.conf.urls import patterns, url

from my_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^permission/(?P<id>\d+)$', views.permission, name='permission')   
)