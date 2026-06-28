from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_calculadoras, name='menu_calculadoras'),
    path('interes-compuesto/', views.interes_compuesto, name='interes_compuesto'),
    path('cuota-prestamo/', views.cuota_prestamo, name='cuota_prestamo'),
    path('conversor-moneda/', views.conversor_moneda, name='conversor_moneda'),
    path('ahorro-objetivo/', views.ahorro_objetivo, name='ahorro_objetivo'),
]