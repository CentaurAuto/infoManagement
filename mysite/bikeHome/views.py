from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from .models import Vehicle
from django.template import loader
from django.urls import reverse
from django.views import generic
from forms import VehicleForm
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

# Create your views here.
@csrf_protect

def mainIndex(request):
	return render(request,'bikeHome/index.html')

def index(request):
	latest_vehicles_list=Vehicle.objects.order_by('-customer_purchase_date')[:10]
	context={'latest_vehicles_list':latest_vehicles_list,}
	return render(request,'bikeHome/bikeHomeIndex.html',context)

def dashboard(request,vehicle_id):
	vehicle=get_object_or_404(Vehicle,vehicle_id=vehicle_id)
	system_status=[vehicle.system_1(),vehicle.system_2(),vehicle.system_3(),vehicle.system_4(),vehicle.system_5(),vehicle.system_6(),vehicle.system_7()]
	for item in range(0,len(system_status)):
		if system_status[item]==True:
			system_status[item]='Good'
		else:
			system_status[item]='Bad'
	return render(request,'bikeHome/dashboard.html',{'vehicle':vehicle,'system_status':system_status})
	
	
def service(request,vehicle_id):
	vehicle=get_object_or_404(Vehicle,vehicle_id=vehicle_id)
	return render(request,'bikeHome/service.html',{'vehicle':vehicle})

def requestPage(request,vehicle_id):
	vehicle=get_object_or_404(Vehicle,vehicle_id=vehicle_id)
	instance = vehicle
	if request.POST:
		form=VehicleForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('../')
	else:
		form=VehicleForm(instance=instance)
	
	return render(request,'bikeHome/request.html',{'vehicle':vehicle,'form':form})	

