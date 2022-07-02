from django.contrib import admin

from .models import Teacher, TeacherPayment

# Register your models here.
admin.site.register(Teacher)
admin.site.register(TeacherPayment)
