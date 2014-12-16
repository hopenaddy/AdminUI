from django.conf.urls import patterns, url
from loginsys import views

urlpatterns = patterns('',
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^check/$', views.auth_check, name='auth_check'),
    url(r'^authorize/$', views.authorize, name='authorize')
)    