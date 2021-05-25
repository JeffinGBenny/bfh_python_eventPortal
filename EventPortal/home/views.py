from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import EventDetails,User_Details
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if User_Details.objects.filter(username=username).exists():
            if User_Details.objects.filter(username=username).exists():
                details=EventDetails.objects.all()
                return render(request,"bfhpage2org.html",{'details':details})
        
            else:
               messages.info(request,'invalid credentials')

    return render(request,"login.html")

def UserProfile(request):
     return render(request,"UserProfile.html")

def  createEvent(request):
    if request.method=='POST':
        eventtitle=request.POST['eventtitle']
        Date=request.POST['Date']
        Time=request.POST['Time']
        Location=request.POST['Location']
        max_no_participants=request.POST['max_no_participants']
        Description=request.POST['Description']
        eventbanner=request.POST['eventbanner']
        print(max_no_participants)
        event1= EventDetails(eventtitle=eventtitle,Date=Date,Time=Time,Location=Location,max_no_participants=max_no_participants,Description=Description,eventbanner=eventbanner)
        event1.save()
        return render(request,"bfhpage2org.html")
        print(max_no_participants)
    else:
         return render(request,"Eventgenerator.html")

def  signup(request):
    if request.method=='POST':
        username=request.POST['username']
        semester=request.POST.get('semester')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST['password']
        if User_Details.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('/')
        else:
            user=User_Details(username=username,password=password,semester=semester,mobile=mobile,email=email)
            user.save()
            messages.info(request,'user created')
            return render(request,"login.html")

    else:
        return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render(request,"login.html")

def  showEvent(request):
    if request.method=='GET':
        
        details=EventDetails.objects.all()
        return render(request,"upcomingorg.html",{'details':details})
    else:
        return redirect("/")
def eventRegister(request):
    
        details=EventDetails.objects.all()
        return render(request,"upcomingorg.html",{'details':details})
        messages.info(request,'Successfully Registered')
        registeredevent=request.POST['registeredevent']
    