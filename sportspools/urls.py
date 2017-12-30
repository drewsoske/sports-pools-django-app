from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='/'),
    url(r'^hockey/', views.nhl, name='nhl'),
    url(r'^nhl/', views.nhl, name='nhl'),
    url(r'^nba', views.nba, name='nba')
]
