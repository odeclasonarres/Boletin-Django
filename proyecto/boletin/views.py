# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, RegModelForm
from .models import Registrado
# Create your views here.
def inicio(request):
    titulo="Hola JUANMA"
    if request.user.is_authenticated():
        titulo="Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    context= {
        "saludo": titulo,
        "el_form":form,
        }
    if form.is_valid():
        instance=form.save(commit=False)
        nombre=form.cleaned_data.get("nombre")
        email=form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre="PERSONA"
        instance.save()
        context = {
            "saludo":"Gracias %s" %(nombre),
        }
        if not instance.nombre:
            context={
                "titulo":"Gracias %s" %(email)
            }
        print instance
        print instance.timestamp
        #form_data=form.cleaned_data
        #nombre1= form_data.get("nombre")
        #abc=form_data.get("email")
        #obj=Registrado.objects.create(email=abc, nombre=nombre1)
    return render(request, "inicio.html", context)

def contact(request):
    form= ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
        # for key in form.cleaned_data:
        #     print key
        #     print form.cleaned_data.get(key)
        form_email=form.cleaned_data.get("email")
        form_mensaje=form.cleaned_data.get("mensaje")
        form_nombre=form.cleaned_data.get("nombre")
        mail_asunto='Form de contacto'
        mail_mensaje= "%s dice:%s . Enviado por: %s" %(form_nombre, form_mensaje, form_email)
        mail_email_from=settings.EMAIL_HOST_USER
        mail_email_to=[mail_email_from, "jmsalcedoserrano@gmail.com"]
        send_mail(mail_asunto,
            mail_mensaje,
            mail_email_from,
            mail_email_to,
            fail_silently=False
        )
        # print email, mensaje, nombre
    context={
        "form":form,
    }
    return render(request, "forms.html", context)
