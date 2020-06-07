from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
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
