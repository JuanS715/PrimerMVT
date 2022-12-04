from django.db import models


class Familiares(models.Model):
    nombre= models.CharField(max_length=10)
    dni=models.CharField(max_length=8, default="")
    fecha=models.CharField(max_length=20, default="")



    def __str__(self):
        
        return (self.nombre) (self.fecha)
    
    


