from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
# Create your views here.

def createFamiliares(request):
    familiar1= Familiares(nombre="Juan", dni=12345678, fecha="09/07/2001" )
    familiar2= Familiares(nombre="Giussepe", dni=12345678, fecha="05/08/1997")
    familiar3= Familiares(nombre="Godofredo", dni=12345678, fecha="03/01/1970")
    familiar1.save
    familiar2.save
    familiar3.save
    traduct= f"Bien hecho {familiar1.nombre} {familiar1.dni} {familiar1.fecha}", f"Bien hecho {familiar2.nombre}, {familiar2.dni} {familiar2.fecha}", f"Bien hecho {familiar3.nombre} {familiar3.dni} {familiar3.fecha}"
    

    return HttpResponse(traduct)
    



|