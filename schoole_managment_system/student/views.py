import math
import random
from random import Random

from django.shortcuts import render

from .models import Student


def student(request):
   if request.method =="POST":
      student_id = request.POST.get('student_id')
      password = request.POST.get('password')

      all_student_data = Student.objects.all()

      for data in all_student_data:
         if data.student_id==student_id and data.password==password:
            return render(request,'student/data.html',{"student":data})
         else:
            return render(request,'student/index.html',{"data":{"data":"Not Found Your Data"}})
   return render(request,'student/index.html')

def student__registations(request):
   if request.method =="POST":
      id = int(random.random()*1000)
      profile_image = request.POST.get('profile_image')
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      class_number = request.POST.get('class_number')
      roll_number = request.POST.get('roll_number')
      phone_number = request.POST.get('phone_number')
      email_address = request.POST.get('email_address')
      enter_your_admin_id = request.POST.get('admin_id')
      present_address = request.POST.get('present_address')
      permanent_address = request.POST.get('permanent_address')
      password = request.POST.get('password')
      re_password = request.POST.get('re_password')

      student_id = f'{first_name}-{last_name}-{id}'
      
      data = Student(id,profile_image,student_id,first_name,last_name,class_number,roll_number,phone_number,email_address,present_address,permanent_address,password,re_password)

      data.save()

   return render(request,'student/registations.html')
