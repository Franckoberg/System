from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^getUser/', views.getUser),
    # url(r'^getUserById/(?P<id>\d+)/$', views.getUserById, name='getUserById'),
    url(r'^getUserById/(?P<id>[0-9]+)/$', views.getUserById, name='getUserById'),
    url(r'^register', views.register),
]