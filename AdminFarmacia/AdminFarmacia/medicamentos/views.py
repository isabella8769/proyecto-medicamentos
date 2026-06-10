from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Medicamento, Movimiento
from .forms import MedicamentoForm, MovimientoForm
from datetime import date


# ==========================
# VISTAS DE MEDICAMENTO
# ==========================

def lista_medicamentos(request):
    q = (request.GET.get('q') or '').strip()

    medicamentos = Medicamento.objects.all()

    if q:
        # Buscar por cualquier característica convirtiendo a string en DB.
        # Incluye: nombre, lote, proveedor, estado, fecha_vencimiento y cantidad.
        medicamentos = medicamentos.filter(
            Q(nombre__icontains=q) |
            Q(lote__icontains=q) |
            Q(proveedor__icontains=q) |
            Q(estado__icontains=q) |
            Q(fecha_vencimiento__icontains=q) |
            Q(cantidad__icontains=q)
        )

    medicamentos = medicamentos.order_by('fecha_vencimiento')
    return render(
        request,
        'medicamentoshtml/lista_medicamentos.html',
        {
            'medicamentos': medicamentos,
            'q': q,
        },
    )



def crear_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            medicamento = form.save()
            messages.success(request, f'Medicamento "{medicamento.nombre}" creado exitosamente.')
            return redirect('inventario:lista_medicamentos')
    else:
        form = MedicamentoForm()
    return render(request, 'medicamentoshtml/crear_medicamento.html', {'form': form})


def detalle_medicamento(request, pk):

    medicamento = get_object_or_404(Medicamento, pk=pk)
    movimientos = medicamento.movimientos.all().order_by('-fecha')[:10]  # últimos 10 movimientos
    return render(request, 'medicamentoshtml/detalle_medicamento.html', {
        'medicamento': medicamento,
        'movimientos': movimientos
    })


def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento actualizado exitosamente.')
            return redirect('inventario:detalle_medicamento', pk=medicamento.pk)
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'medicamentoshtml/editar_medicamento.html', {'form': form, 'medicamento': medicamento})

def eliminar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        nombre = medicamento.nombre
        medicamento.delete()
        messages.success(request, f'Medicamento "{nombre}" eliminado.')
        return redirect('inventario:lista_medicamentos')
    return render(request, 'medicamentos/eliminar_medicamento.html', {'medicamento': medicamento})

# ==========================
# VISTAS DE MOVIMIENTO
# ==========================

def lista_movimientos(request):
    movimientos = Movimiento.objects.all().order_by('-fecha')
    return render(request, 'movimientos/lista_movimientos.html', {'movimientos': movimientos})

def crear_movimiento(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            medicamento = movimiento.medicamento

            # Actualizar stock según tipo
            if movimiento.tipo == 'Ingreso':
                medicamento.cantidad += movimiento.cantidad
            elif movimiento.tipo == 'Egreso':
                if medicamento.cantidad < movimiento.cantidad:
                    messages.error(request, 'Error: No hay suficiente stock.')
                    return redirect('inventario:crear_movimiento')
                medicamento.cantidad -= movimiento.cantidad

            # Actualizar estado
            if medicamento.fecha_vencimiento < date.today():
                medicamento.estado = 'Vencido'
            elif medicamento.cantidad == 0:
                medicamento.estado = 'Agotado'
            else:
                medicamento.estado = 'Activo'

            medicamento.save()
            movimiento.save()

            messages.success(request, f'Movimiento registrado: {movimiento.tipo} de {movimiento.cantidad} unidades.')
            return redirect('inventario:lista_movimientos')
    else:
        form = MovimientoForm()
    return render(request, 'movimientos/crear_movimiento.html', {'form': form})

def detalle_movimiento(request, pk):
    movimiento = get_object_or_404(Movimiento, pk=pk)
    return render(request, 'movimientos/detalle_movimiento.html', {'movimiento': movimiento})

# ==========================
# VISTA DE STOCK (Resumen)
# ==========================

def ver_stock(request):
    medicamentos = Medicamento.objects.all()
    total_stock = sum(med.cantidad for med in medicamentos)
    medicamentos_bajos = medicamentos.filter(cantidad__lt=10)  # menos de 10 unidades
    return render(request, 'medicamentos/ver_stock.html', {
        'medicamentos': medicamentos,
        'total_stock': total_stock,
        'medicamentos_bajos': medicamentos_bajos
    })



