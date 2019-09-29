from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import ProData,StoryData
from .forms import RegistrationForm
import datetime as dt
date1=dt.datetime.now()


def home(request):
    if request.session.get('active'):
       sdata = StoryData.objects.all()
       img = ProData.objects.filter(uname='{0}'.format(request.session.get('active')))
       return render(request, 'login.html', {'img': img, 'sdata': sdata})

    else:
       return render(request, 'home.html')


def registration_view(request):

    try:
            form = RegistrationForm(request.POST,request.FILES or None)
            context = {
                'form': form
            }
            if form.is_valid():
                print(form.cleaned_data)

                name = form.cleaned_data.get('name')
                contact = form.cleaned_data.get('contact')
                uname = form.cleaned_data.get('uname')
                email = form.cleaned_data.get('email')
                password1 = form.cleaned_data.get('password1')
                password2 = form.cleaned_data.get('password2')
                image = form.cleaned_data.get('image')
                data = ProData(
                   name=name,
                   contact=contact,
                   uname=uname,
                   email=email,
                   password1=password1,
                   password2=password2,
                   image=image )
                data.save()
                s="Registration is Successful!!"
                return render(request,'home.html',{'s': s})
            return render(request, 'reg.html',context)

    except:
               i="Please Fill All Fields!!"
               form = RegistrationForm()
               return render(request, 'reg.html', {'form': form,'i': i})


def login_view(request):
        if request.method == "POST":
                uname = request.POST.get('uname')
                password = request.POST.get('password1')

                uname1 = ProData.objects.filter(uname=uname)
                pwd = ProData.objects.filter(password1=password)
                if uname1 and pwd:
                    request.session.set_test_cookie()
                    request.session['active'] = uname
                    img=ProData.objects.filter(uname=uname)
                    sdata=StoryData.objects.all()
                    return render(request,'login.html',{'img':img,'sdata':sdata})
                else:
                    x="Invalid User Data!"
                    return render(request,'home.html',{'x': x})
        else:
            return render(request, 'home.html')


def family(request):
    if request.session.get('active'):
        alldata = ProData.objects.all()
        return render(request,'family.html',{'alldata':alldata})
    else:
        return render(request, 'home.html')


def member(request):
    if request.session.get('active'):
        alldata=ProData.objects.all()
        return render(request, 'member.html', {'alldata':alldata})
    else:
        return render(request, 'home.html')


def success_view(request):
    if request.session.get('active'):
        sdata = StoryData.objects.all()
        img=ProData.objects.filter(uname='{0}'.format(request.session.get('active')))
        return render(request, 'login.html',{'img':img,'sdata':sdata})
    else:
        return render(request, 'home.html')


def link(request):
    try:
       del request.session['active']
    except:
        pass
    finally:
      return render(request, 'home.html')


def storypad(request):
    if request.session.get('active'):
        if request.method == "POST":
            story = request.POST.get('story')
            data = StoryData(story=story, date=date1, )
            data.save()
            sdata = StoryData.objects.all()
            img = ProData.objects.filter(uname="{0}".format(request.session.get('active')))
            return render(request, 'login.html', {'sdata': sdata, 'img': img})
        else:
            sdata = StoryData.objects.all()
            img = ProData.objects.filter(uname="{0}".format(request.session.get('active')))
            return render(request, 'login.html', {'sdata': sdata, 'img': img})
    else:
          return render(request, 'home.html')
def reset(request):
    try:
        if request.method=="POST":
            uname=request.POST.get('uname')
            password1=request.POST.get('password1')
            npassword1=request.POST.get('npassword1')
            npassword2=request.POST.get('npassword2')
            uname=ProData.objects.filter(uname=uname)
            pwd=ProData.objects.filter(password1=password1)
            pwd2=ProData.objects.filter(password2=password1)
            if uname and pwd:
                if npassword1==npassword2:
                    pwd.update(password1=npassword1)
                    pwd2.update(password2=npassword2)
                    c="Your Password Reset Is Successful!!"
                    return render(request,'home.html',{'c': c})
                else:
                    d="New Password Should Match!!"
                    return render(request,'home.html',{'d': d})
            else:
                e="Invalid User Data!!"
                return render(request,'home.html',{'e': e })
        return render(request,'home.html')
    except:
        f="Enter Valid Details!!"
        return render(request,'home.html',{'f': f })
def forget(request):
    try:
        if request.method=="POST":
            uname=request.POST.get('uname')
            email=request.POST.get('email')
            uname5=ProData.objects.filter(uname=uname)
            mdata=ProData.objects.filter(email=email)
            if uname5 and mdata:
                udata=uname5
                return render(request,'home.html',{'udata': udata})
            else:
                g="Enter Valid Details!!!"
                return render(request,'home.html',{'g': g })
        return render(request, 'home.html')
    except:
        h="Invalid Data Entered!!"
        return render(request,'home.html',{'h': h})



