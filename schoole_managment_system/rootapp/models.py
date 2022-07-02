# from calendar import day_name

from django.db import models


# Create your models here.
class Day(models.Model):
   title = models.CharField(max_length=20)
   def __str__(self):
      return self.title

class Class(models.Model):
   title = models.CharField(max_length=20)
   def __str__(self):
      return self.title

class SubjectName(models.Model):
   class_number = models.ForeignKey(Class,on_delete=models.SET_NULL, null=True)
   title = models.CharField(max_length=20)
   def __str__(self):
      return f'{self.class_number.title} {self.title} '


class Notice(models.Model):
   title = models.CharField(max_length=100)
   decpritions = models.TextField(max_length=1500)
   date = models.DateTimeField()

   def __str__(self):
      return f'{self.title}  {self.date} '

class Month(models.Model):
   title = models.CharField(max_length=20)
   def __str__(self):
      return self.title


# Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday


