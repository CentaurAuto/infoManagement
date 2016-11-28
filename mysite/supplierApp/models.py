from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Supplier(models.Model):
	supplier_id=models.CharField(max_length=11,primary_key=True)
	supplier_name=models.CharField(max_length=30)
	supplier_mail_id=models.EmailField(max_length=30)
	supplier_phone_number=models.CharField(max_length=15)
	supplier_latitude=models.DecimalField(max_digits=8,decimal_places=6)
	supplier_longitude=models.DecimalField(max_digits=8,decimal_places=6)
	def __str__(self):
		return self.supplier_id

class System(models.Model):
	supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
	system_name=models.CharField(max_length=30)
	system_lead_time=models.DecimalField(max_digits=10,decimal_places=3)
	system_volume_per_unit=models.DecimalField(max_digits=10,decimal_places=3)
	system_MOQ=models.IntegerField(default=100)
	system_cost_per_system=models.DecimalField(max_digits=10,decimal_places=3)
	ordered_quantity=models.IntegerField(default=100)
	order_ETA=models.DecimalField(max_digits=10,decimal_places=3)

	def __str__(self):
		return self.system_name



