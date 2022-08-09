from django.db import models


# Create your models here.
class Status(models.Model):
   status = models.CharField(max_length=20)
   def __str__(self):
      return self.status


class Institute(models.Model):
   title = models.CharField(max_length=20)
   eni = models.CharField(max_length=10)
   address = models.TextField(max_length=150)
   id = models.CharField(primary_key=True,max_length=10)

   def __str__(self):
      return f'{self.title} {self.eni}'  
