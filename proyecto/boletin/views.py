# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import RegForm
from .models import Registrado
# Create your views here.
def inicio(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data=form.cleaned_data
        nombre1= form_data.get("nombre")
        abc=form_data.get("email")
        obj=Registrado.objects.create(email=abc, nombre=nombre1)
    context= {
        "el_form":form,
    }
    return render(request, "inicio.html", context)
