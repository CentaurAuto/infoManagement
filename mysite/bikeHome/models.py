from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from datetime import timedelta,datetime

now=datetime.now(timezone.utc)


# Create your models here.

class Vehicle(models.Model):
	vehicle_id=models.CharField(max_length=11,primary_key=True)
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



