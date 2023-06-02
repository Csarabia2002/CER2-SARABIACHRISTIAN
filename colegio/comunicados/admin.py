from django.contrib import admin
from .models import Comunicado, Categoria
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Comunicado)
