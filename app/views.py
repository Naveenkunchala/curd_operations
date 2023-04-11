from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
from app.models import *

# Create your views here.

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
    lo=Webpage.objects.all().order_by('name')
    lo=Webpage.objects.all().order_by('-name')
    lo=Webpage.objects.all().order_by(Length('name'))
    lo=Webpage.objects.all().order_by(Length('name').desc())
    lo=Webpage.objects.all()[:2:]
    lo=Webpage.objects.all()[1:2:]
    lo=Webpage.objects.all()
    lo=Webpage.objects.filter(name__regex='[a-zA-Z]{6}')
    lo=Webpage.objects.filter(name__startswith='h')
    lo=Webpage.objects.filter(url__endswith='.com')
    lo=Webpage.objects.filter(name__contains='n')
    lo=Webpage.objects.filter(name__in=('Anil','hari'))
    lo=Webpage.objects.filter(Q(topics_name='chess') & Q(name='Anil'))
    lo=Webpage.objects.filter(Q(topics_name='valley ball'))
    d={'Webpage':lo}
    return render(request,'display_webpages.html',context=d)


def display_arecords(request):
    lo=AccessRecords.objects.all()
    lo=AccessRecords.objects.filter(date__gt='2001-8-22')
    lo=AccessRecords.objects.filter(date__gte='2001-8-22')
    lo=AccessRecords.objects.filter(date__lt='2001-8-22')
    lo=AccessRecords.objects.filter(date__lte='2001-8-22')
    lo=AccessRecords.objects.filter(date__year='2001')
    lo=AccessRecords.objects.filter(date__month='8')
    lo=AccessRecords.objects.filter(date__day='28')
    lo=AccessRecords.objects.filter(date__day__lt='2')
    lo=AccessRecords.objects.filter(date__day__gt='2')
    lo=AccessRecords.objects.all()
    



    d={'AccessRecords':lo}
    return render(request,'display_arecords.html',context=d)

