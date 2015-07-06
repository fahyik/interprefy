"""interprefy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from tbox import views

urlpatterns = [
	url(r'^room/(?P<session_name>[\w\-]+)/$', views.room, name="room"),
	url(r'^gentoken/$', views.gen_token, name="gen_token"),
	url(r'^createsession/$', views.create_session, name="create_session"),
	url(r'^call_center/$', views.call_center, name="call_center"),
]
