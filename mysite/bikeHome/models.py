from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from datetime import timedelta,datetime

now=datetime.now(timezone.utc)


# Create your models here.

class System(models.Model):
	system_name=models.CharField(max_length=30)
	system_id=models.CharField(max_length=11)


	def __str__(self):
		return self.system_name

class SubSystem(models.Model):
	system=models.ForeignKey(System,on_delete=models.CASCADE)
	subsystem_name=models.CharField(max_length=30)

	def __str__(self):
		return self.subsystem_name


class Supplier(models.Model):
	supplier_name=models.CharField(max_length=20)
	system=models.ManyToManyField(System)
	supplier_id=models.CharField(max_length=11,primary_key=True)
	supplier_mail_id=models.EmailField(max_length=30)
	supplier_phone_number=models.CharField(max_length=15)
	supplier_latitude=models.DecimalField(max_digits=8,decimal_places=6)
	supplier_longitude=models.DecimalField(max_digits=8,decimal_places=6)

	def __str__(self):
		return self.supplier_name

class Batch(models.Model):
	order_no=models.CharField(max_length=20)
	supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
	system=models.OneToOneField(System)
	order_lead_time=models.DecimalField(max_digits=10,decimal_places=3)
	order_volume_per_unit=models.DecimalField(max_digits=10,decimal_places=3)
	order_MOQ=models.IntegerField(default=100)
	order_cost_per_system=models.DecimalField(max_digits=10,decimal_places=3)
	ordered_quantity=models.IntegerField(default=100)
	order_ETA=models.DecimalField(max_digits=10,decimal_places=3)
	order_received=models.BooleanField(default=False)
	rejected_quantity=models.IntegerField(default=0)
	class Meta:
		verbose_name_plural = "Batches"

	def __str__(self):
		return self.order_no


class Vehicle(models.Model):
	vehicle_id=models.CharField(max_length=20,primary_key=True)
	batch=models.ManyToManyField(Batch)
	customer_name=models.CharField(max_length=30)
	customer_mail_id=models.EmailField(max_length=30)
	customer_phone_number=models.CharField(max_length=15)
	customer_latitude=models.DecimalField(max_digits=8,decimal_places=6)
	customer_longitude=models.DecimalField(max_digits=8,decimal_places=6)
	customer_purchase_date=models.DateTimeField()
	distance_rode=models.DecimalField(max_digits=6,decimal_places=2)
	battery_soh=models.DecimalField(max_digits=5,decimal_places=2)
	service_status=models.IntegerField(default=1)
	kms_at_previous_service=models.DecimalField(max_digits=6,decimal_places=2)
	time_at_previous_service=models.DateTimeField()
	service_requested=models.BooleanField(default=False)
	problem_requested=models.BooleanField(default=False)

	def kms_to_next_service(self):
		return 4000-self.kms_at_previous_service

	def time_to_next_service(self):
		return (self.time_at_previous_service+timedelta(days=60)-now).days

	def __str__(self):
		return self.vehicle_id


	subsystem_1a=models.BooleanField(default=True)
	subsystem_1b=models.BooleanField(default=True)
	subsystem_1c=models.BooleanField(default=True)
	subsystem_2a=models.BooleanField(default=True)
	subsystem_2b=models.BooleanField(default=True)
	subsystem_2c=models.BooleanField(default=True)
	subsystem_3a=models.BooleanField(default=True)
	subsystem_3b=models.BooleanField(default=True)
	subsystem_3c=models.BooleanField(default=True)
	subsystem_4a=models.BooleanField(default=True)
	subsystem_4b=models.BooleanField(default=True)
	subsystem_4c=models.BooleanField(default=True)
	subsystem_5a=models.BooleanField(default=True)
	subsystem_5b=models.BooleanField(default=True)
	subsystem_5c=models.BooleanField(default=True)
	subsystem_6a=models.BooleanField(default=True)
	subsystem_6b=models.BooleanField(default=True)
	subsystem_6c=models.BooleanField(default=True)
	subsystem_7a=models.BooleanField(default=True)
	subsystem_7b=models.BooleanField(default=True)
	subsystem_7c=models.BooleanField(default=True)
	subsystem_8a=models.BooleanField(default=True)
	subsystem_8b=models.BooleanField(default=True)
	subsystem_8c=models.BooleanField(default=True)	

	def system_1(self):
		if not self.subsystem_1a or not self.subsystem_1b or not self.subsystem_1c:
			return False
		else:
			return True

	def system_2(self):
		if not self.subsystem_2a or not self.subsystem_2b or not self.subsystem_2c:
			return False
		else:
			return True	

	def system_3(self):
		if not self.subsystem_3a or not self.subsystem_3b or not self.subsystem_3c:
			return False
		else:
			return True

	def system_4(self):
		if not self.subsystem_4a or not self.subsystem_4b or not self.subsystem_4c:
			return False
		else:
			return True	

	def system_5(self):
		if not self.subsystem_5a or not self.subsystem_5b or not self.subsystem_5c:
			return False
		else:
			return True

	def system_6(self):
		if not self.subsystem_6a or not self.subsystem_6b or not self.subsystem_6c:
			return False
		else:
			return True

	def system_7(self):
		if not self.subsystem_7a or not self.subsystem_7b or not self.subsystem_7c:
			return False
		else:
			return True

	def system_8(self):
		if not self.subsystem_8a or not self.subsystem_8b or not self.subsystem_8c:
			return False
		else:
			return True				

