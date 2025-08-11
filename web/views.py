from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto

# Create your views here.

def home(request):
    flanes = Producto.objects.all().filter(premium="False")
    return render(request, "web/home.html", {"flanes":flanes})

@login_required
def home_premium(request):
    flanes = Producto.objects.all().filter(premium="True")

    return render(request, "web/home_premium.html", {"flanes":flanes})
