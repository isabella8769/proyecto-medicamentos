from django import forms
from .models import Medicamento, Movimiento


class MedicamentoForm(forms.ModelForm):
    """Formulario para crear/editar medicamentos (Ingreso)"""
    
    class Meta:
        model = Medicamento
        fields = [
            'nombre', 
            'lote', 
            'fecha_vencimiento', 
            'cantidad', 
            'proveedor', 
            'estado'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del medicamento'
            }),
            'lote': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de lote'
            }),
            'fecha_vencimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'  # Selector de fecha
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Cantidad en unidades'
            }),
            'proveedor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del proveedor'
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }


class MovimientoForm(forms.ModelForm):
    """Formulario para registrar movimientos (Ingreso/Egreso)"""
    
    class Meta:
        model = Movimiento
        fields = ['medicamento', 'tipo', 'cantidad', 'motivo']
        widgets = {
            'medicamento': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Cantidad de unidades'
            }),
            'motivo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Motivo del movimiento'
            }),
        }

