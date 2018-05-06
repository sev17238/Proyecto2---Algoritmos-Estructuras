#Proyecto 2, Algoritmos y estructuras de datos
#Prototipo del programa principal para la
#recomendacion de videojuegos.
#------------------Integrates------------------
# - Diego Sevilla 17348
# - David Soto 17551
# - Alejandro Tejada 17854

from Functions import *

#--------Declaramos variables------------------
valorMaximo = 0
listaRecomendaciones = []
listaJuegos = ["Mortal Combat","Super Smash Bros","Dragon Ball Fighters","PacMan","Contra, The Alien Wars","Sonic the Hedgehog","Mario Bros","MegaMan X","Donkey Kong","Kirby","Quake","Halo","Call of Duty","Grand Theft Auto","Gears of War","Dead Space","Metal Slug","Space Invaders","R-type","Age Of Empires","Star Craft","War Craft","Civilization IV","Empire Total War","Advance Wars","Worms","Angry Birds","Gun Bound","MarioKart","Need For Speed","Iron Warriors","H.A.W.X.","Assault Horizon","Mine Craft","Clash of Clans","Gigies Skylines","ANNO","SimCity","Banished","F-Zero","Out Run","Proyect CARS","FIFA Series","Mario Strikers","WiiSports","Wii Fit","Mario & Sonic in the olimpyc games","The legend of Zelda","Tomb Rider","God of war","Silent Hill","The last of Us","Resident Evil","Assassins Creed","MetalGear","Dishonored","StarWars","Final Fantasy","Pokemon","Dungeon & Dragons","Watch Dogs","Horizon Zero Dawn","Prototype","Candy Crush","Tetris","Portal","ZUMA","Q.U.B.E.","Lips","Sing it Disney","Dance Central","JustDance","Guitar HERO","DJ HERO","Rock Revolution"]
listaCoincidencias = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
desicion = 0

#--------Iniciamos el menu----------------------
while desicion != 2:
    valorMaximo = 0
    listaRecomendaciones = []
    listaCoincidencias = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#-------------Se pregunta si desea una recomendacion-----------------    
    print ("\nQue desea hacer?\n1.Recomendar videojuegos\n2.Salir de la aplicacion")
    desicion = int(input("Ingrese su elecccion: "))

    if(desicion == 1):
#------------------Se toma la caracteristica de la persona----------------        
        print("\nQue tipo de persona se considera?\n1.Extrovertida\n2.Introvertida\n3.Atrevida")
        caracteristicas = int(input("Ingrese su eleccion: "))

        if(caracteristicas == 1):
            caracteristica = "Extrovertida"
        elif(caracteristicas == 2):
            caracteristica = "Introvertida"
        elif(caracteristicas == 3):
            caracteristica = "Atrevida"

        listaCoincidencias = RecomendacionCaracteristica(caracteristica,listaJuegos,listaCoincidencias)
#------------------Se toma la inteligencia cognitiva de la persona----------------        
        print("\nQue inteligencia considera que se relaciona mas con usted?\n1.Logica\n2.Espacial\n3.Motora\n4.Musical-Ritmica")
        inteligencias = int(input("Ingrese su eleccion: "))

        if(inteligencias == 1):
            inteligencia = "Logica"
        elif(inteligencias == 2):
            inteligencia = "Espacial"
        elif(inteligencias == 3):
            inteligencia = "Motora"
        elif(inteligencias == 4):
            inteligencia = "Musical-Ritmica"
        
        listaCoincidencias = RecomendacionInteligencia(inteligencia,listaJuegos,listaCoincidencias)
#------------------Se toma la edad de la persona----------------
        print("\nCual es su edad? Elija un rango de edad\n1.4-11 anos\n2.12-17 anos\n3.18-70 anos\n4.Sin especificar")
        edades = int(input("Ingrese su eleccion: "))

        if(edades == 1):
            edad = "4-11"
        elif(edades == 2):
            edad = "12-17"
        elif(edades == 3):
            edad = "18-70"
        elif(edades == 4):
            edad = "Todas las Edades"
        
        listaCoincidencias = RecomendacionEdad(edad,listaJuegos,listaCoincidencias)
#------------------Se toma el genero de videojuego de la persona----------------
        print("\nElija el genero de videojuegos que mas le llama la atencion\n1.Accion\n2.Disparos\n3.Estrategia\n4.Simulacion\n5.Deporte\n6.Aventura\n7.Rol\n8.SandBox\n9.Puzzle\n10.Musical")
        generos = int(input("Ingrese su eleccion: "))

        if(generos == 1):
            genero = "ACCION"
        elif(generos == 2):
            genero = "DISPAROS"
        elif(generos == 3):
            genero = "ESTRATEGIA"
        elif(generos == 4):
            genero = "SIMULACION"
        elif(generos == 5):
            genero = "DEPORTE"
        elif(generos == 6):
            genero = "AVENTURA"
        elif(generos == 7):
            genero = "ROL"
        elif(generos == 8):
            genero = "SANDBOX"
        elif(generos == 9):
            genero = "PUZZLE"
        elif(generos == 10):
            genero = "MUSICAL"
            
        listaCoincidencias = RecomendacionGenero(genero,listaJuegos,listaCoincidencias)
#------------------Se toma el subgenero de videojuego de la persona----------------
        print("\nElija el sub-genero de videojuegos que mas le llama la atencion\n1.Lucha\n2.Arcade\n3.Plataformas\n4.Primera-Persona\n5.Tercera-Persona\n6.ShootemUp\n7.TiempoReal\n8.Turnos\n9.Artilleria\n10.Vehiculos\n11.Construccion\n12.Carreras\n13.AccionAventura\n14.SurvivalHorror\n15.Sigilo\n16.Karaoke\n17.Baile\n18.Instrumentos")
        subgeneros = int(input("Ingrese su eleccion: "))

        if(subgeneros == 1):
            subgenero = "Lucha"
        elif(subgeneros == 2):
            subgenero = "Arcade"
        elif(subgeneros == 3):
            subgenero = "Plataformas"
        elif(subgeneros == 4):
            subgenero = "1raPersona"
        elif(subgeneros == 5):
            subgenero = "3raPersona"
        elif(subgeneros == 6):
            subgenero = "Shoot'em up"
        elif(subgeneros == 7):
            subgenero = "Estrategia en tiempo real"
        elif(subgeneros == 8):
            subgenero = "Estrategia por turnos"
        elif(subgeneros == 9):
            subgenero = "Artilleria"
        elif(subgeneros == 10):
            subgenero = "Simu. Vehiculos"
        elif(subgeneros == 11):
            subgenero = "Simu. Construccion"
        elif(subgeneros == 12):
            subgenero = "Carreras"
        elif(subgeneros == 13):
            subgenero = "Accion-Aventura"
        elif(subgeneros == 14):
            subgenero = "Survival Horror"
        elif(subgeneros == 15):
            subgenero = "Sigilo"
        elif(subgeneros == 16):
            subgenero = "Karaoke"
        elif(subgeneros == 17):
            subgenero = "Baile"
        elif(subgeneros == 18):
            subgenero = "Instrumentos Musicales"
#------------------Se revisa las Coincidencias a lo respondido por el usuario-----------------------            
        listaCoincidencias = RecomendacionSubGenero(subgenero,listaJuegos,listaCoincidencias)

        valorMaximo = max(listaCoincidencias)
#------------------Se da una lista de recomendaciones----------------
        listaRecomendaciones = buscarRecomendacionesFinales(valorMaximo,listaCoincidencias,listaJuegos)
#------------------Se imprimen las recomendaciones-------------------
        print("\nEstas son las recomendaciones de Videojuegos que podrian interesarle al usuario:\n")
        print(listaRecomendaciones)

        




    
