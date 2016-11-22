
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
    url(r'^(?P<vehicle_id>[\w\-]+)/$', views.dashboard, name='dashboard'),
    url(r'^(?P<vehicle_id>[\w\-]+)/service/$',views.service,name='service'),
    url(r'^(?P<vehicle_id>[\w\-]+)/request/$',views.requestPage,name='requestPage'),
]