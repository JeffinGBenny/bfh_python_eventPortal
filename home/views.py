from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
<<<<<<< HEAD
from .models import EventDetails,User_Details
=======
>>>>>>> 3cd566f... success
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
<<<<<<< HEAD
        if User_Details.objects.filter(username=username).exists():
            if User_Details.objects.filter(username=username).exists():
                details=EventDetails.objects.all()
                return render(request,"bfhpage2org.html",{'details':details})
        
            else:
               messages.info(request,'invalid credentials')

    return render(request,"login.html")

def UserProfile(request):
     return render(request,"UserProfile.html")

=======
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return render(request,'bfhpage2org.html')
        else:
            messages.info(request,'invalid credentials')

    return render(request,"login.html")

>>>>>>> 3cd566f... success
def  createEvent(request):
    if request.method=='POST':
        eventtitle=request.POST['eventtitle']
        Date=request.POST['Date']
        Time=request.POST['Time']
<<<<<<< HEAD
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
=======
        max_no_participants=request.POST['max_no_participants']
        Description=request.POST['Description']
        eventbanner=request.POST['eventbanner']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('/')
        else:
            user=User.objects.create_user(username=username,password=password,semester=semester,mobile=mobile,email=email)
            user.save()
            messages.info('user created'
            )

    else:
        return redirect("/")
def  signup(request):
    if request.method=='POST':
        username=request.POST['username']
        semester=request.POST['semester']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('/')
        else:
            user=User.objects.create_user(username=username,password=password,semester=semester,mobile=mobile,email=email)
            user.save()
            messages.info('user created')
>>>>>>> 3cd566f... success

    else:
        return render(request,'signup.html')
def logout(request):
    auth.logout(request)
<<<<<<< HEAD
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
    
=======
    return redirect('/')
    def  showEvent(request):
        if request.method=='GET':
            eventtitle=request.GET['eventtitle']
            Date=request.GET['Date']
            Time=request.GET['Time']
            max_no_participants=request.GET['max_no_participants']
            Description=request.GET['Description']
            eventbanner=request.GET['eventbanner']
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,password=password,semester=semester,mobile=mobile,email=email)
                user.save()
                messages.info('user created'
                )

        else:
            return redirect("/")
>>>>>>> 3cd566f... success