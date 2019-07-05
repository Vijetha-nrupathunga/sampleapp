from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth import authenticate,login,logout
from . forms import UserRegistrationForm 
# Create your views here.

def home_view(request):
    return render(request,'testpage.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    registered=False
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
            return redirect('/')
        else: print(user_form.errors)
    else:
        user_form=UserRegistrationForm()
    return render(request,'auth/register.html',{'form':user_form,'value':'signup','registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse('your account was inactive')
        else:
            print('someone tried to login and failed')
            print('They used username:{} and password:{}'.format(username,password))
            return HttpResponse('invalid login details given')
    else:
        return render(request,'auth/login.html',{})            
