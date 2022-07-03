from django.db import models
from rootapp.models import Month


# Create your models here.
class Teacher(models.Model):
   profile_image = models.ImageField(upload_to='teacher-profile-image/',blank=False)
   teacher_id = models.CharField(max_length=15)
   first_name = models.CharField(max_length=15)
   last_name = models.CharField(max_length=15)
   phone_number = models.CharField(max_length=14)
   email_address = models.CharField(max_length=30)
   present_address = models.TextField(max_length=1000)
   permanent_address = models.TextField(max_length=1000)
   password = models.CharField(max_length=100)
   re_password = models.CharField(max_length=100)

   def __str__(self):
      return f'{self.first_name} {self.last_name}'


class TeacherPayment(models.Model):
   teacher_id = models.CharField(max_length=15)
   payment_in_date = models.DateField()
   payment_month = models.ForeignKey(Month,on_delete=models.SET_NULL, null=True)
   payment_amount = models.CharField(max_length=100000)

   
