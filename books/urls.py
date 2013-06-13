from django.conf.urls import patterns, url

from books import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^results/$', views.results, name='results'),
	url(r'^profile/', views.profile, name='profile'),
)
