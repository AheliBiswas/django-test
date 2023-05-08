from django.shortcuts import render,redirect
from .forms import CustomerForm,AddressForm,CarForm
from .models import Customer
from django.contrib import messages
# Create your views here.
def customerPage(request):
    if request.method=='POST':
        customer = Customer.objects.create(
            firstname = request.POST.get('firstname'),
            lastname= request.POST.get('lastname'),
            age= request.POST.get('age'),
            DOB=request.POST.get('dob'),
            phone_no = request.POST.get('phone_no'),
            email=request.POST.get('email')
        )
        customer.save()
        messages.success(request, "Customer Information Has Been Added Successfully")


    context = {}
    return render(request,'customer.html',context)

def addressPage(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Address Information Has Been Added Successfully")
            form = AddressForm()
    context = {'form':form}
    return render(request,'address.html',context)

def carsPage(request):
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Car Information Has Been Added Successfully")
            form = CarForm()
    context = {'form':form}
    return render(request,'cars.html',context)