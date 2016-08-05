from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^dashboard/$', views.dashboard, name="dashboard"),
	url(r'^about/$', views.about, name="about"),
]