from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic.edit import CreateView

# Create your views here.


def home(request):
    context= dict()

    return render(request,'base/home.html',context)