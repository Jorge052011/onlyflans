
from django.urls import path
from .views import home,home_premium, ProductoDetalle

urlpatterns = [
    path('', home, name = 'home'),
    path('premium/', home_premium, name = 'premium'),
    path("producto/<int:pk>", ProductoDetalle.as_view(), name="detalle")
]


