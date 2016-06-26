# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from agendapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.consulta,name="home"),
    url(r'^consulta/$',views.consulta,name="home"),
    url(r'^contato/new/$', views.contato_new, name='contato_new'),
    url(r'^contato/(?P<pk>[0-9]+)/$', views.contato_detail, name='contato_detail'),
    url(r'^contato/(?P<pk>[0-9]+)/edit/$', views.contato_edit, name='contato_edit'),
    url(r'^contato/(?P<pk>[0-9]+)/delete/$', views.contato_delete, name='contato_delete'),
]
