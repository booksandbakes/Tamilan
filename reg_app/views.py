from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from reg_app import serializers
from rest_framework import viewsets
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserLoginForm, UserRegisterForm, Displayform
from .models import publish,Userdata,image,TopUser
from reg_app import models,forms
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count
def login_view(request):
    logout(request)
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        if request.POST:
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/index')
    context = {'form': form, }
    return render(request, "login.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password1 = form.cleaned_data.get('password1')
        user.set_password(password1)
        user.save()
        new_data=Userdata(Username=request.POST['username'],Email=request.POST['email'],Password1=request.POST['password1'],Password2=request.POST['password2'],City=request.POST['city'])
        new_data.save()
        emailto=request.POST['email']
        name=request.POST['username']
        msg='Hello '+name
        send_mail(msg,
                   "Thank-You for using our Website kindly refer to other peoples ,Mail us if you have any Problem in Our Website.Thank-You Once again" ,
                    settings.EMAIL_HOST_USER,
                    [emailto])
        
        if next:
            return redirect(next)            
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')
def home(request):
    return render(request,'home.html')

def index(request):
    form = publish.objects.filter(Userid=request.user.email)
    data=Displayform()
    context={'form':form, 'data':data }
    return render(request,'index.html',context)

@require_POST      #only post (submit button)
def add(request):
    form=Displayform(request.POST)
    if form.is_valid():
        new_todo=publish(Userid=Userdata.objects.get(Email=request.user.email),tittle=request.POST['title'],contend=request.POST['text'])
        new_todo.save()
    return redirect('index')

def about(request):
    form=TopUser.objects.all()
    img=image.objects.order_by('id')
    li=[]
    for i in form:
        li.append(i.mail1)
    name1=[str(i.Username) for i in Userdata.objects.filter(Email=li[0])]
    city1=[i.City for i in Userdata.objects.filter(Email=li[0])]
    name2=[i.Username for i in Userdata.objects.filter(Email=li[1])]
    city2=[i.City for i in Userdata.objects.filter(Email=li[1])]
    name3=[i.Username for i in Userdata.objects.filter(Email=li[2])]
    city3=[i.City for i in Userdata.objects.filter(Email=li[2])]
    
    context={'name1':name1,'city1':city1,'name2':name2,'city2':city2,'name3':name3,'city3':city3,'form':img}
    return render(request,'about.html',context)

def dis(request,tittle,contend):
    context={'tittle':tittle,'contend':contend}
    return render(request,'single.html',context)

    
def display(request):
    form=publish.objects.all()
    context={'form':form, }
    return render(request,'POST.html',context)

class HeroViewSet(viewsets.ModelViewSet):
    queryset = models.publish.objects.all()
    serializer_class = serializers.userdataSerializer

class MainDataViewset(viewsets.ModelViewSet):
   queryset=models.Userdata.objects.all()
   serializer_class=serializers.createDateBaseSerializer 


import operator
def top(request):
    x1=dict()
    z=[i.Userid for i in publish.objects.all()]
    for i in z:
        x=publish.objects.filter(Userid=i).count()
        x1[i]=x
    
    d=sorted(x1.items(),key=operator.itemgetter(1),reverse=True)
    context={'count':d }
    return render(request,'top.html',context)

def profile(request):
    if request.user.is_authenticated:
        form = publish.objects.filter(Userid=request.user.email)
        data=Displayform()
        context={'form':form, 'data':data }
        return render(request,'index.html',context)
    else:
        return render(request,'profile.html')
    