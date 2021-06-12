from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/")
def explore(request):
    if request.method == "POST":
        caption = request.POST.get('caption')
        file = request.FILES.get('file')
        obj = Post.objects.create(caption=caption,file=file,type="image",user=request.user)
        return render(request,'home.html',{'obj':obj})
    return render(request,'home.html',{})
