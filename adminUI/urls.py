from django.conf.urls import patterns, include, url
from django.contrib import admin
from my_app import views

urlpatterns = patterns('',
    url(r'^$', views.main_page),
    url(r'^users/', include('my_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
