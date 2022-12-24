from django.shortcuts import render, HttpResponse
from datetime import datetime
from suvigya.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is HomePage")
    
def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is AboutPage")

def services(request):
    return HttpResponse("This is ServicesPage")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name,email=email,phone=phone)
        contact.save()
    return render(request,'contact.html')