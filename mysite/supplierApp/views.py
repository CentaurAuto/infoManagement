from django.shortcuts import render,get_object_or_404
from .models import Supplier,System
# Create your views here.

def supplierIndex(request):
	supplier_list=Supplier.objects.all()
	context={'supplier_list':supplier_list,}
	return render(request,'supplierApp/supplierIndex.html',context)

def supplierDashboard(request,supplier_id):
	supplier=get_object_or_404(Supplier,supplier_id=supplier_id)
	return render(request,'supplierApp/dashboard.html',{'supplier':supplier})
	