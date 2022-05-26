from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth import authenticate,login as loginuser
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        user = request.user
        print('>>>>>>>>>>> user', user)
        form = ResultsForm()
        student_result = Results.objects.filter()
        context = {
            'student_result': student_result,
            'form': form
        }
        print('>>>>>>>>>>> context', context)
        return render(request, 'index.html', context=context)


def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        context = {
            'form': form
        }
        return render(request, 'signup.html', context=context)
    else:
        print('>>>>>>>>>> ',request.POST)
        form = SignupForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            user = form.save()
            print('>>>>>>>>>>>> user :   ', user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html',context=context)


def login(request):
    if request.method == 'GET':
        form_auth = AuthenticationForm()
        context = {
            'form': form_auth
        }
        return render(request, 'login.html', context=context)
    else:
        form_auth = AuthenticationForm(data=request.POST)
        print('>>>>>>>>>>>>>>>>>>> form_auth = AuthenticationForm()', form_auth)
        if form_auth.is_valid():
            username = form_auth.cleaned_data.get('username')
            password = form_auth.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                loginuser(request, user)
                return redirect('/')


def loggedout(request):
    logout(request)
    return redirect('/')


def results(request):
    pass


def subjects(request):
    if request.user.is_authenticated:
        user = request.user
        print('>>>>>>>>>>> user', user)
        form = SubjectForm()
        subject = Subject.objects.all()
        context = {
            'subject': subject,
            'form': form
        }
        print('>>>>>>>>>>> context', context)
        return render(request, 'subjects.html', context=context)


@login_required(login_url='login')
def add_subject(request):
    if request.user.is_authenticated:
        user = request.user
        print('>>>>>>>>>>> user', user)
        form = SubjectForm(data=request.POST)
        if form.is_valid():
            print('>>>>>>>>>>>>>>>>>>>', form.cleaned_data)
            l = form.save()
            l.user = user
            l.save()
            return redirect('/subjects')
        else:
            return render(request, 'subjects.html', context={'form':form})


def delete_subject(request, id):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>. id ', id)
    Subject.objects.get(pk=id).delete()
    return redirect('/')


def edit_subject(requuest, id):
    sub = Subject.object.get(pk=id)
    sub.save()
    return redirect('/subjects')