from django.urls import path
from . import views

app_name='Home'

urlpatterns= [
    path('',views.home,name='Home'),
    path('accion/',views.boton,name='boton'),
]