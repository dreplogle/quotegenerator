from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/result$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<pk>[0-9]+)/detail$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<svalue>[A-Za-z]+)/search/$', views.search, name='search'),
    url(r'^search$', views.search, name='search'),
]
