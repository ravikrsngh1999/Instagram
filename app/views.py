from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout,get_user_model
from post.models import *
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("/explore/")
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
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect("/explore/")
    return render(request,'signup.html')


def user_logout(request):
    logout(request)
    return redirect("/")




def profile(request):
    print("inside profile")
    userinfo_obj = UserInfo.objects.get(user = request.user)
    all_posts = Post.objects.filter(user=request.user).order_by("-pk")
    context = {
        'userinfo_obj':userinfo_obj,
        'all_posts':all_posts,
    }
    return render(request,'profile.html',context)


def editprofile(request):
    print("inside editprofile")
    userinfo_obj = UserInfo.objects.get(user = request.user)
    all_posts = Post.objects.filter(user=request.user).order_by("-pk")
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        user_obj = request.user
        user_obj.first_name = name
        user_obj.save()
        bio = request.POST.get("bio")
        userinfo_obj.bio = bio
        userinfo_obj.save()
        try:
            user_obj = User.objects.get(username = username)
            return redirect("/editprofile/")
        except Exception as e:
            user_obj = request.user
            user_obj.username = username
            user_obj.save()

            return redirect('/profile/')
        pass
    context = {
        'userinfo_obj':userinfo_obj,
        'all_posts':all_posts,
    }
    return render(request,'editprofile.html',context)



def deletepost(request,pk):
    post = Post.objects.get(pk=int(pk))
    post.delete()
    userinfo_obj = UserInfo.objects.get(user=request.user)
    userinfo_obj.no_of_posts = userinfo_obj.no_of_posts - 1
    userinfo_obj.save()
    return redirect("/editprofile/")


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
