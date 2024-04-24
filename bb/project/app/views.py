from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import UserRegisterForm
from .models import *
from django.conf import settings
from django.contrib.auth.models import User

def home(request):
    template = loader.get_template('home.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

def index(request):
    template2 = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template2.render(context,request))
#------------
#Registration
#-------------
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
#--------------
# mail system
#--------------
            htmly = get_template('email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'jabir25264@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ################################################################## 
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title':'register here'})
#------  
#login 
#------
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        global user
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home.html')
        else:
            messages.info(request, f'account do not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})
#---------
#logout
#---------
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#-------------
#blood_types
#------------

def blood_types(request):
    template = loader.get_template('blood_types.html')
    context = {

    }
    return HttpResponse(template.render(context,request))
#-------------
#blood_stocks
#-------------

def blood_stocks(request):
    bloodStocks = Blood_stock.objects.all().values()
    template = loader.get_template('blood_stocks.html')
    context = {
        'bloodStocks' : bloodStocks,
    }
    return HttpResponse(template.render(context,request))

#-------------
#blood donor
#-------------

def blood_donor(request):
    if request.user.is_authenticated:
        blood_donate_hos = BloodDonor_hospitals.objects.all().values()
        blood_donate_org = BloodDonor_organisation.objects.all().values()
        template = loader.get_template('blood_donor.html')
        context = {
            'blood_donate_hos':blood_donate_hos,
            'blood_donate_org':blood_donate_org
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseRedirect('/login/')

#--------------
#need blood
#--------------

def need_blood(request):
    if request.user.is_authenticated:
        template = loader.get_template('need_blood.html')
        context={
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseRedirect('/login/')

#----------------
# A+ (need blood)
#----------------
    
def a_plus(request):
    a = Blood_stock.objects.filter(bloodGroup='A+').values()
    template = loader.get_template('a_plus.html')
    context={
        'a':a,
    }
    return HttpResponse(template.render(context,request))

#----------------
# A- (need blood)
#----------------

def a_minus(request):
    a = Blood_stock.objects.filter(bloodGroup='A-').values()
    template = loader.get_template('a_minus.html')
    context={
        'a':a,
    }
    return HttpResponse(template.render(context,request))

#----------------
# B+ (need blood)
#----------------

def b_plus(request):
    a = Blood_stock.objects.filter(bloodGroup='B+').values()
    template = loader.get_template('b_plus.html')
    context={
        'a':a,
    }
    return HttpResponse(template.render(context,request))



#----------------
# B- (need blood)
#----------------

def b_minus(request):
    a = Blood_stock.objects.filter(bloodGroup='B-').values()
    template = loader.get_template('b_minus.html')
    context={
        'a':a,
    }
    return HttpResponse(template.render(context,request))

#----------------
# AB+ (need blood)
#----------------

def ab_plus(request):
    a = Blood_stock.objects.filter(bloodGroup='AB+').values()
    template = loader.get_template('ab_plus.html')
    context={
        'a':a,
    }
    return HttpResponse(template.render(context,request))

#----------------
# AB- (need blood)
#----------------

def ab_minus(request):
    a = Blood_stock.objects.filter(bloodGroup='AB-').values()
    template = loader.get_template('ab_minus.html')
    context={
        'a':a,
    }
    return HttpResponse(template.render(context,request))

#----------------
# O+ (need blood)
#----------------

def o_plus(request):
    a = Blood_stock.objects.filter(bloodGroup='O+').values()
    template = loader.get_template('o_plus.html')
    context={
        'a':a,
    }
    return HttpResponse(template.render(context,request))

#----------------
# O- (need blood)
#----------------

def o_minus(request):
    a = Blood_stock.objects.filter(bloodGroup='O-').values()
    template = loader.get_template('o_minus.html')
    context={
        'a':a,
    }
    return HttpResponse(template.render(context,request))



def eml(request):
    if request.method == "POST":
        h_mail = request.POST.get('tomail')
        if h_mail=='None': 
            messages.success(request, f'Invalid email')
            return HttpResponseRedirect('need_blood')
        else:
            h_mail = request.POST.get('tomail')
            bgrp = request.POST.get('bgrp')
            content = "I have seen in your site that your hospital having blood group "+bgrp+" ,I am in need of it so please kindly reply me to my email for further🤝."
            send_mail("MESSAGE FROM JIF BLOOD DONATES",content,settings.EMAIL_HOST_USER,[h_mail])
            messages.success(request, f'Email sent to {h_mail}')
            return HttpResponseRedirect('need_blood')

def d_mail(request):
    if request.method == "POST":
        hos_mail = request.POST.get('hos_mail')
        if hos_mail == 'None':
            messages.success(request,f'Invalid email')
            return HttpResponseRedirect('blood_donor')
        else:
            hos_mail = request.POST.get('hos_mail')
            content = "I am ready to donate my blood as I have seen your post in JIF blood donate website."
            send_mail("Alert",content,settings.EMAIL_HOST_USER,[hos_mail])
            messages.success(request,f'Email sent to {hos_mail}')
            return HttpResponseRedirect('blood_donor')
        

