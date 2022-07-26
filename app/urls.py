from django.urls import path
from app.views import index, crear_tarea

app_name = 'laboratorio'

urlpatterns =[
    path('', index, name="index"),
]
