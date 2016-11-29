
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^supplier/$',views.supplierIndex,name='supplierIndex'),
	url(r'^supplier/(?P<supplier_id>[\w\-]+)/$', views.supplierDashboard, name='supplierDashboard'),
	]