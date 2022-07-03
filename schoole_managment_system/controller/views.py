import random

from django.shortcuts import render
from rootapp.models import Notice

from .models import Admin


# Create your views here.
def controller(request):

   if request.method =="POST":
      admin_id = request.POST.get('admin_id')
      password = request.POST.get('password')

      all_admin_data = Admin.objects.all()

      for data in all_admin_data:
         if data.admin_id==admin_id and data.password==password:
            return render(request,'controller/data.html',{"admin":data})
         else:
            return render(request,'controller/index.html',{"data":{"data":"Not Found Your Data"}})
   return render(request,'controller/index.html')


def controller_reistations(request):
   if request.method == "POST":
      
      profile_image = request.POST.get("profile_image")
      first_name = request.POST.get("first_name")
      last_name = request.POST.get("last_name")
      phone_number = request.POST.get("phone_number")
      email_address = request.POST.get("email_address")
      present_address = request.POST.get("present_address")
      permanent_address = request.POST.get("permanent_address")
      password = request.POST.get("password")
      re_password = request.POST.get("re_password")
      id = int(random.random()*1000)
      admin_id = f'{first_name}-{last_name}-{id}'

      data = Admin(id,profile_image,admin_id,first_name,last_name,phone_number,email_address,present_address,permanent_address,password,re_password)
      data.save()

   return render(request,'controller/registations.html')
