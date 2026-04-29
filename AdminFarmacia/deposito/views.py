from collections import defaultdict
from tempfile import template
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from matplotlib.style import context
from .models import *

# Create your views here.
def inicio(request):
    return render(request, 'pagina_base/inicio.html')

# funciones para deposito
def lista_deposito(request):
     deposito = Deposito.objects.all().values()
     template = loader.get_template('lista_deposito.html')
     context = {
     'deposito': deposito,
    }
     return HttpResponse(template.render(context, request))

def alta_deposito(request):
    if request.method == 'POST':
        deposito = Deposito(descripcion=request.POST['descripcion'])
        deposito.save()
        return redirect('lista_deposito')
    return render(request, 'lista_deposito.html')

def eliminacion_deposito(request, id_deposito):
    pass

def modificaciones_deposito(request, id_deposito):
    pass

# Funciones para hueco
def lista_hueco(request):
    huecos = Hueco.objects.all()
    return render(request, 'lista_hueco.html', {'huecos': huecos})

def alta_hueco(request):
    pass

def eliminacion_hueco(request, id_hueco):
    pass

def modificaciones_hueco(request, id_hueco):
    pass

# funciones para Supervisor
def lista_supervisor(request):
    supervisores = Supervisor.objects.all()
    return render(request, 'lista_supervisor.html', {'supervisores': supervisores}) 

def alta_supervisor(request):
    pass

def eliminacion_supervisor(request, id_supervisor):
    pass

def modificacion_supervisor(request, id_supervisor):
    pass
