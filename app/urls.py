from django.urls import path
from app.views import index

app_name = 'laboratorio'

urlpatterns =[
    path('', index, name="index"),
]
