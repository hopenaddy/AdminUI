from loginsys import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^check/$', views.auth_check, name='auth_check'),
    url(r'^get_data/$', views.get_data, name='get_data'),
    url(r'^authorize/$', views.authorize, name='authorize')

)    