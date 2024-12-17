
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successflly!!")
            return redirect('login')
        else:
            messages.error(request, "Invalid form data!!")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in.")
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You are now logged out.")
    return redirect('login')

def dashboard(request):
    pass
