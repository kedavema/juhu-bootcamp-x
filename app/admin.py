from django.contrib import admin
from app.models import Laboratorio

# Register your models here.
@admin.register(Laboratorio)
class LabAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    