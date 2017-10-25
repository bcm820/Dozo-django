from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.dash, name='dash'),
    url(r'^assignments/$', views.assignments, name='assignments'),

]