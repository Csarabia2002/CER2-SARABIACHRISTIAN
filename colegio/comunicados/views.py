from django.shortcuts import render
#importe todos los modelos creados de comunicado y categoria
from .models import Comunicado, Categoria
# Create your views here.


#Funcion home encargada de ordenar por ultima fecha de modificacion y renderisar home.html
def home(request):
    comunicados = Comunicado.objects.order_by('-fecha_ultima_modificacion')

    context ={'comunicados':comunicados}

    return render(request, "comunicados/home.html",context)


#Funcion sirve para filtrar los comunicados por nivel , categoria y renderisar comunicado.hmtl 
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

