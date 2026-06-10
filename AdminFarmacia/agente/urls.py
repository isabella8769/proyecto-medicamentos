
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('login-portal/', views.login_portal, name='login_portal'),
    path('panel/', views.panel_principal, name='panel_principal'),

    path('lista_agentes/', views.lista_agentes, name='lista_agentes'),
    path('alta_agentes/',views.alta_agentes,name='alta_agentes'),
    path('eliminacion_agentes/<int:id_agente>/',views.eliminacion_agentes,name='eliminacion_agentes'),
    path('modificaciones_agentes/<int:id_agente>/',views.modificaciones_agentes,name='modificaciones_agentes')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

