from django.conf.urls import url
from . import views

urlpatterns = [

    # ^members/
    url(r'^join/$', views.join, name='join'),
    url(r'^register/$', views.register),
    url(r'^success/$', views.success),

]