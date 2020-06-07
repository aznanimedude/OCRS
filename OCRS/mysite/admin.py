from django.contrib import admin
from mysite.models import Course,Teacher,Student
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
