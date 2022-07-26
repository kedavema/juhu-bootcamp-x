from django.urls import path
from app.views import index, busqueda, detalle_laboratorio


app_name = 'laboratorio'

urlpatterns =[
    path('', index, name="index"),
    path('buscar-estudios-clinicos', busqueda, name="busqueda"),
    path('<slug:nombre_laboratorio>', detalle_laboratorio, name="detalle")
]
