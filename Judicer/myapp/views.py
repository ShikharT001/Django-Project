import re
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
# Create your views here.

from django.http import HttpResponse
from pyautogui import isValidKey

def home(request):
    try:
        # code here
        return render(request,template_name="main.html")
    except Exception as e:
        return HttpResponse(str(e))


def register(request):
    try:
        if request.method == 'POST':
            # username = request.POST.get('username')
            form = UserCreationForm(request.POST)
            if form.isValid():
                user = form.save()
                login(request,user)
                return 'success'
        else:
            form = UserCreationForm()
        return render(request,'register.html',{'form':form})
    except Exception as e:
        return HttpResponse(str(e))

def login(request):
    pass

def dashboard(request):
    pass

def logout(request):
    pass