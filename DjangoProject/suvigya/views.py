from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is HomePage")
    
def about(request):
    return HttpResponse("This is AboutPage")

def services(request):
    return HttpResponse("This is ServicesPage")

def contact(request):
    return HttpResponse("This is ContactPage")