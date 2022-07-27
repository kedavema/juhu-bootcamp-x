import folium
from django.shortcuts import render
from app.models import Laboratorio
from app.utils import ubicaciones 


def index(request):
    return render(request, 'inicio.html')


def busqueda(request):
    center = [-23.485062, -57.741562]
    map = folium.Map(height=500, location=center, zoom_start=5.5)
    
    iframe = folium.IFrame(f'<b>Nombre:</b> Lab San Jose <br> <b>Descripción:</b> Top Lab en Py<br><br> <a target="_blank" href="https://google.com">Ver más</a>', height=90)
    
    popup = folium.Popup(iframe, min_width=300, max_width=300)
    icon = folium.features.CustomIcon('media/images/marker2.png', icon_size=(35, 35))
    map = map._repr_html_()
    if request.method == 'POST':
        map = folium.Map(width=800, height=500, location=[-25.324010, -57.561069], zoom_start=6)
        enfermedad = request.POST['enfermedad']
        ciudad = request.POST['ciudad']
        map = folium.Map(width=800, height=500, location= ubicaciones[ciudad], zoom_start=13)
          
        laboratorios = Laboratorio.objects.filter(estudios_clinicos__enfermedad__nombre=enfermedad)
        for lab in laboratorios:
            iframe = folium.IFrame(f'<b>Nombre:</b> {lab.nombre} <br> <b>Descripción:</b> {lab.descripcion}<br><br> <a target="_blank" href="http://localhost:8000/{lab.slug}">Ver más</a>', height=90)
            popup = folium.Popup(iframe, min_width=300, max_width=300)
            folium.Marker(location=[float(lab.lat), float(lab.long)], popup=popup, icon=icon).add_to(map)
     
            map = map._repr_html_()
        return render(request, 'buscador.html', {'laboratorios': laboratorios, 'map': map})

    return render(request, 'buscador.html', {'map': map})


def detalle_laboratorio(request, nombre_laboratorio):
    laboratorio = Laboratorio.objects.filter(slug=nombre_laboratorio).first()
    return render(request, 'descripcion.html', {"laboratorio": laboratorio})