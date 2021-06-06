from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    #Block of code
    print(request.POST.get('username'))
    print(request.POST.get('password'))
    return render(request,'index.html',)



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
