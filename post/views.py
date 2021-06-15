from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from app.models import *

# Create your views here.

@login_required(login_url="/")
def explore(request):
    all_posts = Post.objects.all().order_by("-pk")
    if request.method == "POST":
        caption = request.POST.get('caption')
        file = request.FILES.get('file')
        type = str(file).split(".")[-1]
        img_types = ["jpg","jpeg","png"]
        if type in img_types:
            type = "image"
        else:
            type="video"
        obj = Post.objects.create(caption=caption,file=file,type=type,user=request.user)
        userinfo_obj = UserInfo.objects.get(user=request.user)
        userinfo_obj.no_of_posts = userinfo_obj.no_of_posts + 1
        userinfo_obj.save()
        return redirect("/")
    return render(request,'home.html',{'all_posts':all_posts})


def getpostdetails(request):
    postid = request.GET.get('postid')
    print(postid)
    post = Post.objects.get(pk=postid)
    l=[]

    l.append(str(post.file))
    l.append(post.user.username)
    l.append(post.caption)
    return JsonResponse(l,safe=False)
