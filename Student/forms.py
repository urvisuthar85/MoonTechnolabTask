from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignupForm(UserCreationForm):
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
    email = forms.EmailField(max_length=64,)
    semester = forms.CharField(max_length=20)
    branch = forms.CharField(max_length=50)
    mobile = forms.CharField(max_length=50)
    enrollno = forms.CharField(max_length=50)
    type = forms.CharField(max_length=50)

    class Meta:
        model = SchoolUser
        fields = ('username', 'semester','branch', 'enrollno', 'mobile', 'email', 'type')

# class Signupform(UserCreationForm):
#         # semester = forms.CharField(max_length=20)
#         # branch = forms.CharField(max_length=50)
#         # mobile = forms.CharField(max_length=50)
#         # enrollno = forms.CharField(max_length=50)
#         # type = forms.CharField(max_length=50)
#         email = forms.EmailField(max_length=50)
#
#     class Meta:
#         model = SchoolUser
#         fields = ('username','password1','password2','email')

    #
    # class Meta:
    #     model = SchoolUser
    #     fields = ('username', 'semester','branch', 'enrollno', 'mobile', 'email', 'password', 'type')


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ('id', 'name')


class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = ('subid', 'stuid', 'marks')