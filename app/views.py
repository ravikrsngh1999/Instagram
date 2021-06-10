from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
# Create your views here.

def home(request):
    #Block of code
    print(request.POST.get('username'))
    print(request.POST.get('password'))
    return render(request,'index.html',)


def signup(request):
    if request.method == "POST":
        print("Request Post")
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        bio = request.POST.get('bio')
        print(username)
        user_obj = User.objects.create(username=username,first_name=name,email=email)
        user_obj.set_password(password)
        user_obj.save()
        print(user_obj)
        user_info_obj = UserInfo.objects.create(phone_number=phone_number,bio=bio,user=user_obj)
        return redirect("/")
    return render(request,'signup.html')

def test(request):
    if request.method == "POST":
        print("POST REQUEST GENERATED")
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        obj = User.objects.create(username=username,first_name=name,email=email)
        obj.set_password(password)
        obj.save()
        print(obj)
        pass
    print("-------------------")
    return render(request,'test.html',)
