from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agente.urls')),
    path('', include('deposito.urls')),
    path('medicamentos/', include(('AdminFarmacia.medicamentos.urls', 'inventario'), namespace='inventario')),
]

