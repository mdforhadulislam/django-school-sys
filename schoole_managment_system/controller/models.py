from django.db import models

# Create your models here.
class Admin(models.Model):
   profile_image = models.ImageField(upload_to='admin-profile-image/',blank=False)
   admin_id = models.CharField(max_length=20)
   first_name = models.CharField(max_length=15)
   last_name = models.CharField(max_length=15)
   phone_number = models.CharField(max_length=14)
   email_address = models.CharField(max_length=30)
   present_address = models.TextField(max_length=1000)
   permanent_address = models.TextField(max_length=1000)
   password = models.CharField(max_length=20)
   re_password = models.CharField(max_length=20)

   def __str__(self):
      return f'{self.first_name} {self.last_name}'
