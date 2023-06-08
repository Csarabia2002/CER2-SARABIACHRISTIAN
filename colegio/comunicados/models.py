from django.db import models
#importo el moderlo user para poder usarlo como variable en el modelo comunicado
from django.contrib.auth.models import User

#modelo.categoria segun en el pdf
class Categoria(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    
    
    def __str__(self):
        return self.nombre


#modelo.comunicado segun en el pdf


class Comunicado(models.Model):
    #creo los niveles para poder usarlos como variables
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
    
