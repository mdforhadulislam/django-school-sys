from http.client import HTTPResponse

from django.shortcuts import render


# Create your views here.
def home(request):
   return render(request,'home.html')

def service(request):
   return render(request,'service.html')

def contact(request):
   return render(request,'contact.html')
