from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registeration(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('registeration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('registeration')
            else:
                user = User.objects.create_user(username=username, first_name=f_name, last_name=l_name, email=email,
                                                password=pass1)
                user.save();
                messages.info(request, "user created")
                return redirect('login')
        else:
            messages.info(request, "Password Mismatch")
            return redirect('registeration')
        return redirect('/')
    return render(request, 'register.html')

def about(request):
  return render(request,'about.html')
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Inavild Credentials')
            return redirect('login')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')