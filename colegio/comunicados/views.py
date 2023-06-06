from django.shortcuts import render
from .models import Comunicado, Categoria
# Create your views here.
def home(request):
    comunicados = Comunicado.objects.order_by('fecha_ultima_modificacion')

    context ={'comunicados':comunicados}

    return render(request, "comunicados/home.html",context)


def filtrar_comunicados(request):
    nivel = request.GET.get('nivel')
    categoria = request.GET.get('categoria')


    comunicados = Comunicado.objects.all()

    if nivel:
        comunicados = comunicados.filter(nivel=nivel)


    if categoria:
        comunicados = comunicados.filter(categoria__nombre=categoria)   


    context = {'comunicados':comunicados,
               'niveles': Comunicado.NIVEL_CHOICES,
               'categorias': Categoria.objects.all()
               }

    return render(request, "comunicados/comunicado.html",context)

