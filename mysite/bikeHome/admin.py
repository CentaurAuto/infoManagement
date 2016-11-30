from django.contrib import admin
from .models import Supplier,Vehicle,System,SubSystem,Batch


admin.site.register(Supplier)
admin.site.register(Vehicle)
admin.site.register(System)
admin.site.register(SubSystem)
admin.site.register(Batch)
