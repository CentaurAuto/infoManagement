from django import forms
from models import Vehicle

class VehicleForm(forms.ModelForm):

	class Meta:
		model=Vehicle
		fields=['subsystem_1a','subsystem_1b','subsystem_1c','subsystem_2a','subsystem_2b','subsystem_2c','subsystem_3a','subsystem_3b','subsystem_3c','subsystem_4a','subsystem_4b','subsystem_4c','subsystem_5a','subsystem_5b','subsystem_5c','subsystem_6a','subsystem_6b','subsystem_6c','subsystem_7a','subsystem_7b','subsystem_7c','subsystem_8a','subsystem_8b','subsystem_8c']