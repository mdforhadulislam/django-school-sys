
from django.contrib import admin

from .models import Class, Day, Month, Notice, SubjectName

# Register your models here.
admin.site.register(Day)
admin.site.register(Class)
admin.site.register(SubjectName)
admin.site.register(Notice)
admin.site.register(Month)
