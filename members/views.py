from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'member':member,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('testing.html')
    context = {
        'fruits':['apple','banana','cherry','mango','kiwi'],
        'fname':'kaleb',
        'members':{}
    }
    return HttpResponse(template.render(context,request))

def testing2(request):
    myData = Member.objects.filter(age__lte=22).order_by('-firstname').values()
    myData2 = Member.objects.filter(firstname__istartswith='H').values()
    myData3 = Member.objects.filter(Q(firstname__iexact='cole') | Q(firstname__iexact='jude')).values()
    template = loader.get_template('testing2.html')
    context = {
        'myData':myData,
        'myData2':myData2,
        'myData3':myData3,
    }
    return HttpResponse(template.render(context,request))

