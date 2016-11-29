
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.mainIndex,name='mainIndex'),
	url(r'^vehicle/$',views.index,name='index'),
    url(r'^vehicle/(?P<vehicle_id>[\w\-]+)/$', views.dashboard, name='dashboard'),
    url(r'^vehicle/(?P<vehicle_id>[\w\-]+)/service/$',views.service,name='service'),
    url(r'^vehicle/(?P<vehicle_id>[\w\-]+)/request/$',views.requestPage,name='requestPage'),
]