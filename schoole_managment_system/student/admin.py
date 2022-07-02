from django.contrib import admin

from .models import (ExamRoutine, SingleRoutine, Student, StudentAttendence,
                     StudentPayment)

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentPayment)
admin.site.register(StudentAttendence)
admin.site.register(SingleRoutine)
admin.site.register(ExamRoutine)
