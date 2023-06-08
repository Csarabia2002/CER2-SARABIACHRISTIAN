"""
URL configuration for colegio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#lo que hice fue importar todas las views de la app comunicados y se importan dos views
from comunicados.views import home, filtrar_comunicados

#se configuran las urls de home y de filtrar comunicados
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = "home"),
    path('filtrar_comunicados/',filtrar_comunicados, name= "filtrar_comunicados")

]
