# TODO: Fix alta_deposito - ACTUALIZADO ✅

## Cambios:
1. ✅ Template lista_deposito.html: Enlace corregido `{% url 'alta_deposito' %}` 
2. ✅ View alta_deposito: GET renderiza alta_deposito.html, POST guarda y redirige

## Prueba:
- /lista_deposito/ → click Agregar → /alta_deposito/ (form)
- Submit → nuevo depósito en lista

**Nota:** El log muestra user aún clickea /lista_deposito/alta_deposito/ - con enlace {% url %} irá a /alta_deposito/ correcto. Recarga servidor para ver cambios en template.

Comando servidor Windows: `cd AdminFarmacia` enter, luego `python manage.py runserver`

