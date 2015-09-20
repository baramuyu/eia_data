from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[^/]+)/$', views.DetailView.as_view(), name='detail')
]