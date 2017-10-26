from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.dash, name='dash'),
    url(r'^assignments/$', views.assignments, name='assignments'),
    url(r'^addtoplans/(?P<id>\d+)/$', views.addtoplans, name='addtoplans'),
    url(r'^remfromplans/(?P<id>\d+)/$', views.remfromplans, name='remfromplans'),
    url(r'^commit/$', views.commit, name='commit'),

]