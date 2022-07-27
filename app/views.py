import folium
from django.shortcuts import render
from app.models import Laboratorio
from app.utils import ubicaciones 


def index(request):
    """Función principal de nuestra aplicación"""
    return render(request, 'inicio.html')


def busqueda(request):
    """Función principal de búsqueda de laboratorios y mapa"""
    # Generamos el centro del mapa
    center = [-23.485062, -57.741562]
    # Generamos el mapa
    map = folium.Map(height=500, location=center, zoom_start=5.5)
    # Creamos el icono personalizado
    icon = folium.features.CustomIcon('media/images/marker2.png', icon_size=(35, 35))
    # Convertimos el mapa a un tipo html
    map = map._repr_html_()
    if request.method == 'POST':
        map = folium.Map(width=800, height=500, location=[-25.324010, -57.561069], zoom_start=6)
        # Obtenemos los datos del formulario
        enfermedad = request.POST['enfermedad']
        ciudad = request.POST['ciudad']
        
        map = folium.Map(width=800, height=500, location=ubicaciones[ciudad], zoom_start=12)
        # Filtramos todos los laboratorios que tengan la enfermedad
        laboratorios = Laboratorio.objects.filter(estudios_clinicos__enfermedad__nombre=enfermedad)
        # Por cada laboratorio que cumpla el filtro, agregamos un marcador
        for lab in laboratorios:
            # Creamos el iframe para el popup
            iframe = folium.IFrame(f'<b>Nombre:</b> {lab.nombre} <br> <b>Descripción:</b> {lab.descripcion}<br><br> <a target="_blank" href="http://localhost:8000/{lab.slug}">Ver más</a>', height=90)
            popup = folium.Popup(iframe, min_width=300, max_width=300)
            # Agregamos el marcador al mapa
            folium.Marker(location=[float(lab.lat), float(lab.long)], popup=popup, icon=icon).add_to(map)
            map = map._repr_html_()
        return render(request, 'buscador.html', {'map': map})
    return render(request, 'buscador.html', {'map': map})


def detalle_laboratorio(request, nombre_laboratorio):
    """Detalle de un laboratorio"""
    laboratorio = Laboratorio.objects.filter(slug=nombre_laboratorio).first()
    return render(request, 'descripcion.html', {"laboratorio": laboratorio})