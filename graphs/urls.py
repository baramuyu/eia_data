from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>.*)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<category_id>.*)/vote/$', views.vote, name='vote'),
]