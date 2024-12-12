
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.

from django.http import HttpResponse

def home(request):
    try:
        # code here
        return render(request,template_name="main.html")
    except Exception as e:
        return HttpResponse(str(e))


def register(request):

    if request.method == 'POST':
        # username = request.POST.get('username')
        form = UserCreationForm(request.POST)
        if form.is_Valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        init_data = {'username':'','email':'','password':''}
        form = UserCreationForm(init_data)
    return render(request,'register.html',{'form':form})
   

def login(request):
    
    if request.method == 'POST':
        # username = request.POST.get('username')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_Valid():
            login(request, user)
            user = form.get_user()
            return redirect('dashboard')
    else:
        init_data = {'username':'','password':''}
        form = AuthenticationForm(initial=init_data)
    return render(request,'login.html',{'form':form})



def dashboard(request):
    pass

def logout(request):
    logout(request)
    return redirect('login')