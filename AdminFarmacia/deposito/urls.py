from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('deposito/lista_deposito/', views.lista_deposito, name='lista_deposito'),
    path('deposito/alta_deposito/',views.alta_deposito,name='alta_deposito'),
    path('deposito/eliminacion_deposito/<int:id_deposito>/',views.eliminacion_deposito,name='eliminacion_deposito'),
    path('deposito/modificaciones_deposito/<int:id_deposito>/',views.modificaciones_deposito,name='modificaciones_deposito'),
    path('deposito/lista_hueco/',views.lista_hueco, name='lista_hueco'),
    path('deposito/alta_hueco/',views.alta_hueco, name='alta_hueco'),
    path('eliminacion_hueco/<int:id_hueco>',views.eliminacion_hueco, name='eliminacion_hueco'),
    path('modificaciones_hueco/<int:id_hueco>',views.modificaciones_hueco, name='modificaciones_hueco'),
    path('lista_supervisor/',views.lista_supervisor, name='lista_supervisor'),
    path('alta_supervisor/',views.alta_supervisor, name='alta_supervisor'),
    path('eliminacion_supervisor/<int:id_supervisor>',views.eliminacion_supervisor, name='eliminacion_supervisor'),
    path('modificacion_supervisor/<int:id_supervisor>',views.modificacion_supervisor, name='modificacion_supervisor'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)