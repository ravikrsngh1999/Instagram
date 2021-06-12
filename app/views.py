from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout,get_user_model
# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("/explore/")
        else:
            print("Login Failed")    
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







def explore(request):
    return HttpResponse("Login Complete")


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
