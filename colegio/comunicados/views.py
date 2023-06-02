from django.shortcuts import render
from .models import Comunicado
# Create your views here.
def home(request):
    comunicados = Comunicado.objects.order_by('fecha_ultima_modificacion')


    return render(request, "comunicados/home.html", {'comunicados':comunicados})



