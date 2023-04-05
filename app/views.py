from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *


def insert_topic(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topics_names=tn)[0]
    TO.save()
    return HttpResponse('Topic names are inserted successfully')

def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    TO1=Topic.objects.get_or_create(topics_names=tn)[0]
    WO=Webpage.objects.get_or_create(topics_name=TO1,name=n,url=u)[0]
    TO1.save()
    WO.save()
    return HttpResponse('webpage are inserted successfully ')

def insert_access(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    a=input('enter author')
    d=input('enter date')
    TO2=Topic.objects.get_or_create(topics_names=tn)[0]
    WO1=Webpage.objects.get_or_create(topics_name=TO2,name=n,url=u)[0]
    AR=AccessRecords.objects.get_or_create(name=WO1,author=a,date=d)[0]
    TO2.save()
    WO1.save()
    AR.save()
    return HttpResponse('AccessRecords are inserted successfully ')

def display_topic(request):
    lo=Topic.objects.all()
    d={'topics':lo}
    return render(request,'display_topic.html',context=d)


def display_webpages(request):
    lo=Webpage.objects.all()
    d={'Webpage':lo}
    return render(request,'display_webpages.html',context=d)

def display_arecords(request):
    lo=AccessRecords.objects.all()
    d={'AccessRecords':lo}
    return render(request,'display_arecords.html',context=d)

