from django.conf.urls import url
from . import views


app_name = 'clients'
urlpatterns = [
	url(r'^$', views.client_list, name='client_list'),
	url(r'^clients/(?P<client_id>[0-9]+)/$', views.client_detail, name='detail'),
]