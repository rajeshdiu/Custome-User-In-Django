from django.shortcuts import render,redirect
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signinPage(request):
    
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=authenticate(username=username,password=password)
    
        if user:
            login(request,user)
            return redirect("homePage")
    
    return render(request,"signinPage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect("signinPage")

def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        user_type=request.POST.get("user_type")
        age=request.POST.get("age")
        contact=request.POST.get("contact")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        
        if password==confirm_password:
            user=Custom_user.objects.create_user(
                username=username,
                email=email,
                user_type=user_type,
                Age=age,
                Contact_No=contact,
                password=password,
            )
            return redirect("signinPage")
    
    return render(request,"signupPage.html")

@login_required
def homePage(request):

    return render(request,"home.html")

@login_required
def addJobPage(request):
    
    return render(request,"addjobPage.html")
@login_required
def viewJobPage(request):
    
    return render(request,"viewJobPage.html")
