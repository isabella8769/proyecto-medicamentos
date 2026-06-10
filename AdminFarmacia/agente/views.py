from django.shortcuts import render, redirect
from .models import Agente
from django.conf import settings


def inicio(request):
    return render(request, 'pagina_base/inicio.html')


def login_portal(request):
    if request.method != 'POST':
        return redirect('inicio')

    nombre_apellido = request.POST.get('nombre_apellido', '').strip()
    dni = request.POST.get('dni', '').strip()
    cargo = request.POST.get('cargo', '').strip()
    password = request.POST.get('password', '')

    if password != getattr(settings, 'PORTAL_PASSWORD', 'admin123'):
        return render(
            request,
            'pagina_base/inicio.html',
            {'error': 'Contraseña incorrecta.'}
        )

    if not nombre_apellido or not dni or not cargo:
        return render(
            request,
            'pagina_base/inicio.html',
            {'error': 'Completá nombre, DNI y cargo.'}
        )

    request.session['portal_user'] = {
        'nombre_apellido': nombre_apellido,
        'dni': dni,
        'cargo': cargo,
    }
    return redirect('panel_principal')


def panel_principal(request):
    if request.GET.get('salir') == '1':
        request.session.pop('portal_user', None)
        return redirect('inicio')

    if not request.session.get('portal_user'):
        return redirect('inicio')

    return render(request, 'pagina_base/index.html', request.session['portal_user'])



def lista_agentes(request):
    agentes = Agente.objects.all()
    return render(request, 'lista_agentes.html', {'agentes': agentes})

def alta_agentes(request):
    pass

def eliminacion_agentes(request, id_agente):
    pass

def modificaciones_agentes(request, id_agente):
    pass
