from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User

# Create your views here.

def register(request):
    if request.method=='POST':
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2 :
            print('YEEEEEEEEEEEEEEEEEEET', password1,password2)
            if User.objects.filter(email=email).exists() :
                messages.info(request,f'Account {email} already exists :(')
                return redirect('register')
            else:
                user=User.objects.create_user(email,email, password1)
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(email=email, password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
