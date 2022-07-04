from controller.models import Admin
from django.db import models
from rootapp.models import Class, Day, Month, SubjectName


# Create your models here.
class Student(models.Model):
   profile_image = models.ImageField(upload_to='student-profile-image/',blank=False)
   student_id = models.CharField(max_length=15)
   first_name = models.CharField(max_length=15)
   last_name = models.CharField(max_length=15)
   class_number = models.IntegerField()
   roll_number = models.IntegerField()
   phone_number = models.CharField(max_length=14)
   email_address = models.CharField(max_length=30)
   enter_your_admin_id = models.ForeignKey(Admin,on_delete=models.SET_NULL, null=True)
   present_address = models.TextField(max_length=1000)
   permanent_address = models.TextField(max_length=1000)
   password = models.CharField(max_length=100)
   re_password = models.CharField(max_length=100)
   def __str__(self):
      return f'{self.first_name} {self.last_name} {self.roll_number}'


class StudentPayment(models.Model):
   student_id = models.CharField(max_length=15)
   payment_in_date = models.DateField()
   payment_month = models.ForeignKey(Month,on_delete=models.SET_NULL, null=True)
   payment_amount = models.CharField(max_length=100000)

   def __str__(self):
      return f'{self.student_id} {self.payment_month} {self.payment_amount}'


class StudentAttendence(models.Model):
   student_id = models.CharField(max_length=15)
   present_in_date = models.DateField()
   def __str__(self):
      return f'{self.student_id} {self.present_in_date}'




class SingleRoutine(models.Model):
   day_name = models.ForeignKey(Day,on_delete=models.SET_NULL, null=True)
   subject = models.ForeignKey(SubjectName,on_delete=models.SET_NULL, null=True)
   # subject = models.CharField(max_length=50)
   def __str__(self):
      return f'{self.subject.class_number} {self.day_name.title} {self.subject.title}'


class ExamRoutine(models.Model):
   class_number = models.ForeignKey(Class,on_delete=models.SET_NULL, null=True)
   date = models.DateField()
   subject = models.CharField(max_length=100)

   def __str__(self):
      return f'{self.class_number} {self.date} {self.subject}'
 

   # Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
