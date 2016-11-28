
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.supplierIndex,name='supplierIndex'),
	url(r'^(?P<supplier_id>[\w\-]+)/$', views.supplierDashboard, name='supplierDashboard'),
	]