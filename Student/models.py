from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class SchoolUser(AbstractUser):
    semester_choice = [
        ('1', 'FirstSem'),
        ('2', 'SecondSem'),
        ('3', 'ThirdSem'),
        ('4', 'FourthSem'),
    ]
    branch_choice = [
        ('MB', 'Mechanical Branch'),
        ('CE', 'Computer Engineering'),
        ('IT', 'Information technology'),
    ]
    usertype_choice = [
        ('S', 'Student'),
        ('A', 'Admin'),
    ]
    semester = models.CharField(max_length=20, choices=semester_choice)
    branch = models.CharField(max_length=50, choices=branch_choice)
    enrollno = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    usertype = models.CharField(max_length=50, choices=usertype_choice)
    email = models.EmailField()


class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Results(models.Model):
    subid = models.ForeignKey(Subject,on_delete=models.CASCADE)
    stuid = models.ForeignKey(SchoolUser, on_delete=models.CASCADE)
    marks = models.IntegerField()


