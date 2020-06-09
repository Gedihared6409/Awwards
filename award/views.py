from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Project,Profile,Review
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,ProfileForm,GradeForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='Awards'
    post=Project.objects.all()
    profile = Profile.objects.all()
    grade= Review.objects.all()
    current_user=request.user
    return render(request,'AW/home.html',{'title':title ,'post':post,'profile':profile,'current_user':current_user,'grade':grade})

@login_required(login_url='/accounts/login/')
def profile(request,id):
   user_object = request.user
   current_user = Profile.objects.get(username__id=request.user.id)
   user = Profile.objects.get(username__id=id)
   projects = Project.objects.all()
   return render(request, "AW/profile.html", {"current_user":current_user,"projects":projects,"user":user,"user_object":user_object})
