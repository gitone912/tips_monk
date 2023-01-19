from django.shortcuts import render
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
            return render(request, "home.html", {'form':fm,'ans':ans})
    else:
        fm = user_status()
    return render(request, "home.html", {'form':fm})
    