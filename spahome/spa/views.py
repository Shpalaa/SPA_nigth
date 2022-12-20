from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    responce = redirect('home')
    return responce


def home(request):
    bds = Rituals.objects.all()
    bd_care = Body_care.objects.all()
    rsp = Plase.objects.all()
    context = {'bds': bds, 'bd_care': bd_care, 'rsp': rsp}
    return render(request, 'layout/home.html', context)


def spa_menu(request):
    bds = Rituals.objects.all()
    bd_care = Body_care.objects.all()
    files = Save_menu.objects.all()
    context = {'bds': bds, 'bd_care': bd_care, 'files': files}
    return render(request, 'spa_ss/spa_menu.html', context)


def about_us(request):
    return render(request, 'spa_ss/about_us.html')


def masters(request):
    return render(request, 'spa_ss/masters.html')


def qualifications(request):
    return render(request, 'spa_ss/qualifications.html')


def salons(request):
    return render(request, 'spa_ss/salons.html')


def contacts(request):
    return render(request, 'spa_ss/contacts.html')


def certificate(request):
    return render(request, 'spa_ss/certificate.html')


def Sea_SPA(request):
    return render(request, 'spa_ss/Sea_spa.html')
