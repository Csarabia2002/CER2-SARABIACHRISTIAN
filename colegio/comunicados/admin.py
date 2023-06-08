from django.contrib import admin
from .models import Comunicado, Categoria
# Register your models here.
#llevo los modelos a la pagina de admin para poder modificarlos y vizualizarlos 
admin.site.register(Categoria)
admin.site.register(Comunicado)
