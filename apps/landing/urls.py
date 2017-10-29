from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

]