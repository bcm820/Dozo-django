from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.ifttt, name='ifttt'),
    url(r'^start/$', views.start, name='start'),
    url(r'^end/$', views.end, name='end')

]