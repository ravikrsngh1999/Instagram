from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def explore(request):
    return HttpResponse("Login Complete")
