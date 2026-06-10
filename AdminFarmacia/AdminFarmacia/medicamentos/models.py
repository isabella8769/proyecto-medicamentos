from django.db import models

# --- Modelos Existentes ---

class Supervisor(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_apellido

class Deposito(models.Model):
    id_deposito = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
# --- Nuevos Modelos ---

class Medicamento(models.Model):
    # Opciones para el estado del medicamento
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Vencido', 'Vencido'),
        ('Agotado', 'Agotado'),
    ]

    nombre = models.CharField(max_length=200)
    lote = models.CharField(max_length=50, unique=True) # El lote suele ser único
    fecha_vencimiento = models.DateField()
    cantidad = models.PositiveIntegerField(default=0)
    proveedor = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activo')

    # Opcional: Relación con Deposito para saber dónde se guarda
    # deposito = models.ForeignKey(Deposito, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} (Lote: {self.lote})"


class Movimiento(models.Model):
    # Tipos de movimiento
    TIPO_CHOICES = [
        ('Ingreso', 'Ingreso'), # Entrada de stock
        ('Egreso', 'Egreso'),   # Salida de stock
    ]

    medicamento = models.ForeignKey(Medicamento, related_name='movimientos', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.PositiveIntegerField()
    motivo = models.TextField(help_text="Ej: Compra, Donación, Venta, Merma")
    fecha = models.DateTimeField(auto_now_add=True) # Se coloca la fecha actual automáticamente

    def __str__(self):
        return f"{self.tipo} - {self.cantidad} unidades de {self.medicamento.nombre}"





