#Proyecto 2, Algoritmos y estructuras de datos
#Prototipo del programa principal para la
#recomendacion de videojuegos.
#------------------Integrates------------------
# - Diego Sevilla 17348
# - David Soto 17551
# - Alejandro Tejada 17854

from Functions import *

desicion = 0

while desicion != 2:

    print ("\nQue desea hacer?\n1.Recomendar videojuegos\n2.Salir de la aplicacion")
    desicion = int(input("Ingrese su elecccion: "))

    if(desicion == 1):
        
        print("\nQue tipo de persona se considera?\n1.Extrovertida\n2.Introvertida\n3.Atrevida")
        caracteristicas = int(input("Ingrese su eleccion: "))

        if(caracteristicas == 1):
            caracteristica = "Extrovertida"
        elif(caracteristicas == 2):
            caracteristica = "Introvertida"
        elif(caracteristicas == 3):
            caracteristica = "Atrevida"

        Recomendacion(caracteristica)

        




    
