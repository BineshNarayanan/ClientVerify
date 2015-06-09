from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^getclient', views.getClientDetails, name='getclient'),
	url(r'^saveclientresponse', views.saveClientResponse, name='saveclientresponse'),
]