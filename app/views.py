import folium
from django.shortcuts import redirect, render
from django.urls import reverse
from app.models import Enfermedad, EstudioClinico, Laboratorio

def index(request):
    return render(request, 'index.html')


def busqueda(request):
    enfermedades = Enfermedad.objects.all()
    if request.method == 'POST':
        enfermedad = request.POST['enfermedad']
        laboratorios = Laboratorio.objects.filter(estudios_clinicos__enfermedad__nombre=enfermedad)

        map = folium.Map(width=800, height=500, location=[-25.283080, -57.560415], zoom_start=6)
        map = map._repr_html_()
        return redirect(reverse('busqueda', kwargs={'laboratorios': laboratorios, 'map': map }))
    return render(request, 'busqueda.html')


def detalle_laboratorio(request, nombre_laboratorio):
    laboratorio = Laboratorio.objects.filter(slug=nombre_laboratorio)
    return render(request, 'detalle_laboratorio.html', {"laboratorio": laboratorio})

