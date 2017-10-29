from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.dash, name='dash'),
    url(r'^ready/$', views.assignments, name='assignments'),
    url(r'^clear/$', views.clear, name='clear'),
    url(r'^add/(?P<id>\d+)/$', views.addtoplans, name='addtoplans'),
    url(r'^return/(?P<id>\d+)/$', views.remfromplans, name='remfromplans'),
    url(r'^set/$', views.commit, name='commit'),
    url(r'^go/$', views.go, name='go'),
    url(r'^dozo/$', views.dozo, name='dozo'),
    url(r'^archive/$', views.archive, name='archive'),

]