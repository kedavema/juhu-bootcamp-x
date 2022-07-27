from django.contrib import admin
from app.models import Enfermedad, EstudioClinico, Laboratorio

# Register your models here.
@admin.register(Laboratorio)
class LabAdmin(admin.ModelAdmin):
    fields = ['nombre', 'slug', 'descripcion', 'lat', 'long', 'estudios_clinicos']
    

admin.site.register(EstudioClinico)
admin.site.register(Enfermedad)