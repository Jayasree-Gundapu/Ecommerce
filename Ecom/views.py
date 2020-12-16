from django.shortcuts import render
from django.http import HttpResponse
from Ecom.models import Product

# Create your views here.

def index(request):
	p=Product.objects.all()
	context = {'p':p}
	return render(request,'index.html',context)

def detail(request,product_id,slug):
	p = Product.objects.get(id = product_id)
	response=get_response(request)
	context ={'d':d}
	return render(request,'detail.html',context)
