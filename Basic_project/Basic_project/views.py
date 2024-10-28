from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from BasicApp.models import *
from django.core.validators import validate_email
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError



def homePage(req):
    return render(req,'common/home.html')


def registrationPage(req):
    if req.method == 'POST':
        user_name=req.POST.get('name')
        Email=req.POST.get('email')
        User_type=req.POST.get('user_type')
        Password=req.POST.get('psw')
        Confirm_password=req.POST.get('Cpsw')
        
        if not all([user_name,Email,User_type,Password,Confirm_password]):
            messages.warning(req,'All fields are required')
            return render(req,'common/register.html')
        
        try:
            validate_email(Email)
        except ValidationError:
            messages.warning(req,'Invalid Email Format')
            return render(req,'common/register.html')
        if Password != Confirm_password:
            messages.warning(req,'Password do no match')
            return render(req,'common/register.html')
        if len(Password)<8:
            messages.warning(req,'Passwords must be atleast 8 characters long')
            return render(req,'common/register.html')
        if not any(char.isdigit() for char in Password) or not any(char.isalpha() for char in Password):
            messages.warning(req,'Password must contain characters and numbers')
            return render(req,'common/register.html')
        try:
            user=customUser.objects.create_user(
                username=user_name,
                email=Email,
                user_type=User_type,
                password=Password,
            )
   
            messages.success(req,'Successfully Registered')
            return redirect('loginPage')
        except IntegrityError:
            messages.warning(req,'Username or email already exists')
            return render(req,'common/register.html')
    return render(req,'common/register.html')


def loginPage(req):
    if req.method == 'POST':
        user_name=req.POST.get('name')
        Password=req.POST.get('psw')
        if not user_name or not Password:
            messages.warning(req,'Both userbane and password are required')
            return render(req,'common/login.html')
        user = authenticate(
            username=user_name,
            password=Password
        )
        if user is not None:
            login(req,user)
            messages.success(req,'Login Successfully')
            return redirect('homePage')
        else:
            messages.warning(req,'Invalid username or password')
            
    return render(req,'common/login.html')

def logoutPage(req):
    logout(req)
    return redirect('loginPage')
            