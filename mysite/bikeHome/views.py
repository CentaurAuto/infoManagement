from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from .models import Vehicle,Supplier,System,Batch,SubSystem
from django.template import loader
from django.urls import reverse
from django.views import generic
from forms import VehicleForm
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.shortcuts import render,get_object_or_404

# Create your views here.


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
	system_status=[vehicle.system_1(),vehicle.system_2(),vehicle.system_3(),vehicle.system_4(),vehicle.system_5(),vehicle.system_6(),vehicle.system_7(),vehicle.system_8()]
	for item in range(0,len(system_status)):
		if system_status[item]==True:
			system_status[item]='Good'
		else:
			system_status[item]='Bad'
	return render(request,'bikeHome/dashboardVehicle.html',{'vehicle':vehicle,'system_status':system_status})
	
	
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

def supplierIndex(request):
	supplier_list=Supplier.objects.all()
	batches_list=[]
	systems_list=[]
	for supplier in supplier_list:
		batches=Batch.objects.filter(supplier=supplier)
		batches_list.append(batches)
		systems_list.append([])
		for batch in batches:
			batch_system=batch.system
			vehicles=Vehicle.objects.filter(batch=batch)
			systems_list[len(systems_list)-1].append([batch_system,len(vehicles),0])
			for vehicle in vehicles:
				system_status=[vehicle.system_1(),vehicle.system_2(),vehicle.system_3(),vehicle.system_4(),vehicle.system_5(),vehicle.system_6(),vehicle.system_7(),vehicle.system_8()]
				system_name=batch_system.system_name
				if not system_status[int(system_name[len(system_name)-1])-1]:
					systems_list[-1][-1][2]+=1
	main_list=zip(supplier_list,batches_list,systems_list)
	context={'supplier_list':supplier_list,'main_list':main_list}
	return render(request,'bikeHome/indexSupplier.html',context)

def supplierDashboard(request,supplier_id):
	supplier=get_object_or_404(Supplier,supplier_id=supplier_id)
	return render(request,'bikeHome/dashboardSupplier.html',{'supplier':supplier})