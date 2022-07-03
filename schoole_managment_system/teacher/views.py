import random

from django.shortcuts import render

from .models import Teacher


# Create your views here.
def teacher(request):
   if request.method =="POST":
      teacher_id = request.POST.get('teacher_id')
      password = request.POST.get('password')

      all_teacher_data = Teacher.objects.all()

      for data in all_teacher_data:
         if data.teacher_id==teacher_id and data.password==password:
            return render(request,'teacher/data.html',{"teacher":data})
         else:
            return render(request,'teacher/index.html',{"data":{"data":"Not Found Your Data"}})
   return render(request,'teacher/index.html')


def registations(request):
   if request.method=="POST":
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
      teacher_id =f'{first_name}-{last_name}-{id}'
      data = Teacher(id,teacher_id,profile_image,first_name,last_name,email_address,phone_number,present_address,permanent_address,password,re_password)
      data.save()

   return render(request,'teacher/registations.html')
