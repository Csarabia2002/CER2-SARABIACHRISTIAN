from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    
    
    def __str__(self):
        return self.nombre



class Comunicado(models.Model):
    NIVEL_CHOICES =[  
        ("GEN","General"),
        ("PRE","Ciclo Preescolar"),
        ("BAS","Ciclo Basico"),
        ("MED","Ciclo Medio"),
    ]
    
    correlativo = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 50)
    detalle = models.CharField(max_length = 100)
    nivel = models.CharField(max_length = 10, choices = NIVEL_CHOICES)
    categoria = models.ForeignKey('Categoria',on_delete = models.CASCADE )
    fecha_envio = models.DateTimeField(auto_now_add = True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now = True)
    publicado_por = models.ForeignKey(User,on_delete = models.CASCADE)
    

    def __str__(self):
        return self.titulo
    
