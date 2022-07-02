import math
import random
from random import Random

from django.shortcuts import render

# from .models import Student


# Create your views here.
def student(request):
   # if request.method =="POST":
   #    first_name = request.POST.get('first_name')
   #    id = float(random.random()*1000)
   #    data = Student(id,first_name)
   #    data.save()
   return render(request,'student/index.html')
