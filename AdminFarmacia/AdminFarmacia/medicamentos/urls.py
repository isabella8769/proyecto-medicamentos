from django.urls import path
from . import views

app_name = 'medicamentos'

urlpatterns = [
    # --- URLs de Medicamento ---
    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/nuevo/', views.crear_medicamento, name='crear_medicamento'),
    path('medicamentos/<int:pk>/', views.detalle_medicamento, name='detalle_medicamento'),
    path('medicamentos/<int:pk>/editar/', views.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/<int:pk>/eliminar/', views.eliminar_medicamento, name='eliminar_medicamento'),
    
    # --- URLs de Movimiento ---
    path('movimientos/', views.lista_movimientos, name='lista_movimientos'),
    path('movimientos/nuevo/', views.crear_movimiento, name='crear_movimiento'),
    path('movimientos/<int:pk>/', views.detalle_movimiento, name='detalle_movimiento'),
    
    # --- URL de Stock ---
    path('stock/', views.ver_stock, name='ver_stock'),
]