from django.shortcuts import render, redirect
from .models import RegistrationData
from .forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse
def registration_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            fname=request.POST.get('first_name')
            lname = request.POST.get('last_name')
            uname = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            data=RegistrationData(
                first_name=fname,
                last_name=lname,
                username=uname,
                password=password,
                email=email,
                mobile=mobile
            )
            data.save()
            rform=RegistrationForm()
            return render(request,'reg.html',{'rform':rform})
        else:
            return HttpResponse('Invalid Data')
    else:
        rform=RegistrationForm()
        return render(request,'reg.html',{'rform':rform})
def login_view(request):
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            uname=RegistrationData.objects.filter(username=username)
            pwd=RegistrationData.objects.filter(password=password)
            if uname and pwd:
                return redirect('/home/')
        else:
            return HttpResponse('Wrong Details')
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})
def success_view(request):
    return render(request,'success.html')






