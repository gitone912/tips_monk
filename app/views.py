from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth  import authenticate,  login, logout 
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .newai import *
# Create your views here.
def home(request):
    if request.method == "POST":
        fm = user_status(request.POST)
        if fm.is_valid():
            q=fm.cleaned_data['ques']
            ans = tips(str(q))
            print(ans)
            return render(request, "reports.html", {'ans':ans})
    else:
        fm = user_status()
    return render(request, "index.html", {'form':fm})
def Register(request):
    if request.method != "POST":
        return render(request, "register.html")
    username = request.POST['username']
    email = request.POST['email']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 != password2:
        messages.error(request, "Passwords do not match.")
        return redirect('/register')

    user = User.objects.create_user(username, email, password1)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return render(request, 'login.html')

def Login(request):
    if request.method != "POST":
        return render(request, "login.html")
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Logged In")
        return render(request ,'after_login.html')
    else:
        messages.error(request, "Invalid Credentials")
    return render(request ,'after_login.html')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')