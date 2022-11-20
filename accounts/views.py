from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.http import HttpResponse

# Create your views here.


def register(request):

    MIN_LENGTH=8;

    if request.method=='POST':
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2 :
            if len(password1) < MIN_LENGTH:  
                messages.error(request,'Password too short')
                return redirect('register')
            elif User.objects.filter(email=email).exists() :
                messages.error(request,f'Account already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(email,email, password1)
                print(user.id)
                return redirect('login')
        else:
            messages.error(request,'Password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):

    if request.user.is_authenticated:
        redirect('')

    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(username=email, password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            try:
                if User.objects.get(username=email): messages.error(request,'Incorrect Password')             
            except:
                messages.error(request,"Email doesn't exist")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
