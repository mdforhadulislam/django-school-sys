from django.shortcuts import render


# Create your views here.
def login(request):
   return render(request, 'admin/login.html')


def forgetPassword(request):
   return render(request, 'home.html')


def registations(request):
   return render(request, 'home.html')
