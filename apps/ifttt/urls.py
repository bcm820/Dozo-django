from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.sync, name='sync'),
    url(r'^generate/$', views.generate, name='generate'),
    url(r'^start/$', views.start),
    url(r'^end/$', views.end)

]