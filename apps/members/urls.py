from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth

urlpatterns = [

    # members/
    url(r'^join/$', views.join, name='join'),
    url(r'^register/$', views.register),
    url(r'^success/$', views.success, name='success'),

    # members/auth/
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^auth/login/$', auth.login, {'template_name': 'index.html'}, name='login'),

]