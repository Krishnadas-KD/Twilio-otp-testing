from django.shortcuts import render
from .models import *
# Create your views here.
from .serializers import *
from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from django.http import HttpResponse
from django.template import RequestContext
from .form import Createform
from rest_framework.views import View
from twilio.rest import Client
import os
from .key import *
import random
from calendar import c
import threading
from threading import Timer
import schedule
from time import sleep
import time

# Create your views here.
def index(respone,i):
    ls = Details.objects.get(Reg_no=i)
    return HttpResponse("<h1>%s<h1>" %ls.Name)

def home(request):
    return render(request, "mian/P1.html", {})

def create(response):
    if response.method == 'POST':
        form = Createform(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data['name']
            r = form.cleaned_data['regno']
            m = form.cleaned_data['mobilno']
            print(n)
            print(r)
            print(m)
            t = Details(Name=n,Reg_no=r,mobile_no=m)
            t.save()
    else:
        form = Createform()

    return render(response, "mian/home.html", {"form":form})
def SMSsender(response):
    if response.method == 'POST':
        if response.POST.get("Delete"):
                mo=0
                Dtxt=response.POST.get("D_reg")
                if Dtxt=='':
                    return render(response, "mian/std.html", {})
                global d
                if Details.objects.filter(Reg_no=Dtxt).exists():
                    d=Details.objects.get(Reg_no=Dtxt)
                    sn=d.Name
                    pmo=str(d.mobile_no)
                    if len(pmo)!=13:
                        if len(pmo)==12:
                            if pmo[0]==9 and pmo[1]==1:
                                pmo="+"+pmo
                        else:
                            pmo="+91"+pmo
                    global n
                    n=random.randint(10001,99999)
                    s='\n'+sn +'\n Your otp verifiaction code '+str(n)
                    print(s)
                    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                    client.messages.create(from_='+14849862170',
                    to=pmo,
                    body=s)
                    return render(response, "mian/otpv.html", {})
                else:
                    return HttpResponse("<h1>Reg no did not<h1>")
    return render(response, "mian/std.html", {})

def otpverify(response):
    global n
    global d
    if response.method == 'POST':
        if response.POST.get("otpverify"):
            optc=response.POST.get("otp_code")
            if(int(optc) == n):
                print('=============SUCESSFULLY ENTER============')
                del n
                return render(response, "mian/studetails.html", {"d":d})
                del d
            elif optc == "":
                print('=============Time out============')
                del n
                return render(response, "mian/std.html", {"d":d})
                del d
            else:
                del d
                del n
                return render(response, "mian/std.html", {})
    return  render(response, "mian/std.html", {})
    


