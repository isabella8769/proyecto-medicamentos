from collections import defaultdict
from tempfile import template
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

from .models import *


# Create your views here.
def inicio(request):
    return render(request, "pagina_base/inicio.html")


# funciones para deposito
def lista_deposito(request):
    depositos = Deposito.objects.all()
    return render(request, "lista_deposito.html", {"depositos": depositos})


def alta_deposito(request):
    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        if descripcion:  # Validación básica
            deposito = Deposito(descripcion=descripcion)
            deposito.save()
        return redirect("lista_deposito")  # Redirige a la vista que lista depósitos

    # Si es GET, mostramos la lista de depósitos
    depositos = Deposito.objects.all()
    return render(request, "alta_deposito.html", {"depositos": depositos})


def eliminacion_deposito(request, id_deposito):
    deposito = Deposito.objects.get(id_deposito=id_deposito)

    if request.method == "POST":
        deposito.delete()
        return redirect("lista_deposito")

    return render(request, "elimina_deposito.html", {"deposito": deposito})


def modificaciones_deposito(request, id_deposito):
    deposito = Deposito.objects.get(id_deposito=id_deposito)

    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        if descripcion:
            deposito.descripcion = descripcion
            deposito.save()
        return redirect("lista_deposito")

    return render(request, "modificacion_deposito.html", {"deposito": deposito})


# Funciones para hueco
def lista_hueco(request):
    huecos = Hueco.objects.all()
    return render(request, "lista_hueco.html", {"huecos": huecos})


def alta_hueco(request):
    if request.method == "POST":
        # Ajustado a modelos actuales (definidos en medicam.../models.py)
        descripcion = request.POST.get("descripcion") or request.POST.get("nombre")
        if descripcion:
            hueco = Hueco(descripcion=descripcion)
            hueco.save()
        return redirect("lista_hueco")

    huecos = Hueco.objects.all()
    return render(request, "alta_hueco.html", {"huecos": huecos})


def eliminacion_hueco(request, id_hueco):
    hueco = Hueco.objects.get(id_hueco=id_hueco)

    if request.method == "POST":
        hueco.delete()
        return redirect("lista_hueco")

    return render(request, "elimina_hueco.html", {"hueco": hueco})


def modificaciones_hueco(request, id_hueco):
    hueco = Hueco.objects.get(id_hueco=id_hueco)

    if request.method == "POST":
        descripcion = request.POST.get("descripcion") or request.POST.get("nombre")
        if descripcion:
            hueco.descripcion = descripcion
            hueco.save()
        return redirect("lista_hueco")

    return render(request, "modificacion_hueco.html", {"hueco": hueco})


# funciones para Supervisor
def lista_supervisor(request):
    supervisores = Supervisor.objects.all()
    return render(request, "lista_supervisor.html", {"supervisores": supervisores})


def alta_supervisor(request):
    if request.method == "POST":
        nombre_apellido = request.POST.get("nombre_apellido")
        contacto = request.POST.get("contacto")

        if nombre_apellido and contacto:
            supervisor = Supervisor(nombre_apellido=nombre_apellido, contacto=contacto)
            supervisor.save()

        return redirect("lista_supervisor")

    supervisores = Supervisor.objects.all()
    return render(request, "alta_supervisor.html", {"supervisores": supervisores})


def eliminacion_supervisor(request, id_supervisor):
    supervisor = Supervisor.objects.get(id_supervisor=id_supervisor)

    if request.method == "POST":
        supervisor.delete()
        return redirect("lista_supervisor")

    return render(request, "eliminacion_supervisor.html", {"supervisor": supervisor})


def modificacion_supervisor(request, id_supervisor):
    supervisor = Supervisor.objects.get(id_supervisor=id_supervisor)

    if request.method == "POST":
        supervisor.nombre_apellido = request.POST.get("nombre_apellido") or supervisor.nombre_apellido
        supervisor.contacto = request.POST.get("contacto") or supervisor.contacto
        supervisor.save()
        return redirect("lista_supervisor")

    return render(request, "modificacion_supervisor.html", {"supervisor": supervisor})

