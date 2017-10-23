from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth

urlpatterns = [

    url(r'^join/$', views.join, name='join'),
    url(r'^register/$', views.register), # logout
    url(r'^success/$', views.success, name='success'), # temporary until new app
    url(r'^ifttt/$', views.ifttt, name='ifttt')

    # later, have a user profile page
    # return redirect(reverse('users:show', kwargs={'id': your_id_variable }))

]