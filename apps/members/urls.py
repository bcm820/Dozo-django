from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth

urlpatterns = [

    url(r'^join/$', views.join, name='join'),
    url(r'^register/$', views.register),
    url(r'^success/$', views.success, name='success'), # temporary until new app

    # later, have a user profile page
    # return redirect(reverse('users:show', kwargs={'id': your_id_variable }))

]