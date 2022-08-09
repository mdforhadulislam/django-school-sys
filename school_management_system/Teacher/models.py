from django.contrib.auth import get_user_model
from django.db import models
from rootApp.models import Institute, Status


# Create your models here.
class Teacher(models.Model):
   User = get_user_model()

   user = models.ForeignKey(User, on_delete=models.CASCADE)
   teacher_id = models.CharField(max_length=30)
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   profile_image = models.FileField(upload_to='student/')
   institute_name = models.ForeignKey(Institute, on_delete=models.CASCADE)
   mobile_number = models.CharField(max_length=15)
   email_address = models.CharField(max_length=30)
   present_address = models.TextField(max_length=200)
   permanent_address = models.TextField(max_length=200)
   status =  models.ForeignKey(Status, on_delete=models.CASCADE)

   def __str__(self):
      return f'{self.first_name} {self.last_name}'
