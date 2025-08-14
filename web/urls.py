
from django.urls import path
from . import views
from .views import home,home_premium, ProductoDetalle

urlpatterns = [
    path('', home, name = 'home'),
    path('premium/', home_premium, name = 'premium'),
    path("producto/<int:pk>", ProductoDetalle.as_view(), name="detalle"),
    path("acerca/", views.acerca, name="acerca"),
    path("bienvenido/", views.bienvenido_cliente, name="bienvenido_cliente"),
]


