from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login

user=get_user_model()

def register_user(request):
    if request.method=="POST":
        username=request.POST['username']
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm_password"]
        
        if password!=confirm:
            return render(request,'accounts/signup.html',{'error':'Passwords Donot match! Enter a valid password.'})
        
        user.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        return redirect('login')

    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        
        user=authenticate(request,email=email,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('show-book')
        else:
            return render(request,'accounts/login.html',{'error':'Invalid email or password'})
        
    return render(request,'accounts/login.html')        