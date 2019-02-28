# howdy/urls.py
from django.conf.urls import url
from howdy import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name = 'index'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about')
]
