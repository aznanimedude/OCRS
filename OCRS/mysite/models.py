from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    teacher_name = models.CharField(max_length=50)
    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=300)
    students = models.ManyToManyField(Student)
    teacher = models.ManyToManyField(Teacher)
    def __str__(self):
        return self.course_name

class Grade(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    grade = models.PositiveIntegerField()
