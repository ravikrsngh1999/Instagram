from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/")
def explore(request):
    return render(request,'home.html',{})
