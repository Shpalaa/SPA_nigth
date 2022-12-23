from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    responce = redirect('home')
    return responce


def home(request):
    bds = Mountain_Rituals.objects.all()
    bd_care = Mountain_Body_care.objects.all()
    rsp = Plase.objects.all()
    context = {'bds': bds, 'bd_care': bd_care, 'rsp': rsp}
    return render(request, 'layout/home.html', context)


def Mountain_spa_menu(request):
    bds = Mountain_Rituals.objects.all()
    bd_care = Mountain_Body_care.objects.all()
    files = Save_menu.objects.all()
    context = {'bds': bds, 'bd_care': bd_care, 'files': files}
    return render(request, 'spa_ss/Mountain_spa_menu.html', context)


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


def Town_SPA(request):
    bd_rt = Town_SPA_RT.objects.all()
    bd_bc = Town_spa_BC.objects.all()
    context = {'bd_bc': bd_bc, 'bd_rt': bd_rt}
    return render(request, 'spa_ss/Town_spa.html', context)


def Sea_SPA(request):
    bd_rt = Sea_SPA_RT.objects.all()
    bd_bc = Sea_spa_BC.objects.all()
    context = {'bd_bc': bd_bc, 'bd_rt': bd_rt}
    return render(request, 'spa_ss/Sea_spa.html', context)
