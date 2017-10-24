from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^join/$', views.join, name='join'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout_member/$', views.logout_member, name='logout_member')

]