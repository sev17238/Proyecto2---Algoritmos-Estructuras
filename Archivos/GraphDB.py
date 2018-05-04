#Algunas Referencias: https://marcobonzanini.com/2015/04/06/getting-started-with-neo4j-and-python/

#Proyecto 2, Algoritmos y estructuras de datos
#Prototipo de la base de datos basada en grafos
#------------------Integrates------------------
# - Diego Sevilla 17348
# - David Soto 17551
# - Alejandro Tejada 17854

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

#Base de Datos
db = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")

#Principales etiquetas
Caracteristica = db.labels.create("Caracteristica")
Genero = db.labels.create("Genero")
SubGenero = db.labels.create("Subgenero")
VideoJuego = db.labels.create("Videojuego")

#********************Caracteristicas de la persona**************************
#En esta parte se tienen que poner nodos que contengan caracteristicas que
#pueda tener una persona de manera que podamos redirigir esas caracteristicas
#a un genero en especifico de videojuego o a un videojuego en si.
#Podria ser tambien TIPOS DE PERSONAS Ej(Extrovertida,introvertida,etc.)
Extrovertido= db.nodes.create(name="Extrovertida")
Introvertido= db.nodes.create(name="Introvertida")
Atrevido= db.nodes.create(name="Atrevida")

#************************Habilidades de la persona*******************************
'''Logica = db.nodes.create(name="Logica")
Espacial = db.nodes.create(name="Espacial")
Pensar = db.nodes.create(name="Pensar")
Guerras = db.nodes.create(name="Guerras")
Miedo = db.nodes.create(name="Deportes")'''


#******************************GENEROS**************************************
Accion= db.nodes.create(name="ACCION")#1
Disparos= db.nodes.create(name="DISPAROS")#2
Estrategia= db.nodes.create(name="ESTRATEGIA")#3
Simulacion= db.nodes.create(name="SIMULACION")#4
Deporte= db.nodes.create(name="DEPORTE")#5
Aventura= db.nodes.create(name="AVENTURA")#6
Rol= db.nodes.create(name="ROL")#7 
SandBox= db.nodes.create(name="SANDBOX")#8
Puzzle= db.nodes.create(name="PUZZLE")#9
Musical= db.nodes.create(name="MUSICAL")#10

#****************************SUBGENEROS*************************************
#1 ACCION
Lucha= db.nodes.create(name="Lucha")
Arcade= db.nodes.create(name="Arcade")
Plataformas= db.nodes.create(name="Plataformas")
#2 DISPAROS
PraPersona= db.nodes.create(name="1raPersona")
TraPersona= db.nodes.create(name="3raPersona")
ShootemUp= db.nodes.create(name="Shoot'em up")
#3 ESTRATEGIA
TiempoReal= db.nodes.create(name="Estrategia en tiempo real")
Turnos= db.nodes.create(name="Estrategia por turnos")
Artilleria= db.nodes.create(name="Artilleria")
#4 SIMULACION
Vehiculos= db.nodes.create(name="Vehiculos")
Construccion= db.nodes.create(name="Construccion")
#5 DEPORTE
Carreras= db.nodes.create(name="Carreras")
#6 AVENTURA
AccionAventura= db.nodes.create(name="Accion-Aventura")
SurvivalHorror= db.nodes.create(name="Survival Horror")
Sigilo= db.nodes.create(name="Sigilo")
#7 ROL
# No hay subgeneros
#8 SANDBOX
# No hay subgeneros
#9 PUZZLE
# No hay subgeneros
#10 MUSICAL
Karaoke= db.nodes.create(name="Karaoke")
Baile= db.nodes.create(name="Baile")
Instrumentos= db.nodes.create(name="Instrumentos Musicales")

#******************************VIDEOJUEGOS**********************************
#-----------------------ACCION-------------------------
#1.1 lucha
MortalCombat= db.nodes.create(name="Mortal Combat")
SmashBros= db.nodes.create(name="Super Smash Bros")
DragonBall= db.nodes.create(name="Dragon Ball Fighters")
#1.2 arcade
PacMan= db.nodes.create(name="PacMan")
Contra= db.nodes.create(name="Contra, The Alien Wars")
Sonic= db.nodes.create(name="Sonic the Hedgehog")
#1.3 plataformas
Mario= db.nodes.create(name="Mario Bros")
MegaMan= db.nodes.create(name="MegaMan X")
DonkeyKong= db.nodes.create(name="Donkey Kong")
#----------------------DISPAROS------------------------
#2.1 primera persona
Quake= db.nodes.create(name="Quake")
Halo= db.nodes.create(name="Halo") #estrategia, shooter
CallofDuty= db.nodes.create(name="Call of Duty")
#2.2 tercera persona
GrandTheft= db.nodes.create(name="Grand Theft Auto")
GearsWar= db.nodes.create(name="Gears of War")
DeadSpace= db.nodes.create(name="Dead Space")
#2.3 shoot em up
MetalSlug= db.nodes.create(name="Metal Slug")
SpaceInvaders= db.nodes.create(name="Space Invaders")
Rtype= db.nodes.create(name="R-type")
#----------------------ESTRATEGIA-----------------------
#3.1 estrategia en tiempo real
AgeofEmpires= db.nodes.create(name="Age Of Empires")
StarCraft= db.nodes.create(name="Star Craft")
WarCraft= db.nodes.create(name="War Craft")
#3.2 estrategia por turnos
Civilization= db.nodes.create(name="Civilization IV")
EmpireTotalWar= db.nodes.create(name="Empire Total War")
AdvanceWars= db.nodes.create(name="Advance Wars")
#3.3 artilleria
Worms= db.nodes.create(name="Age Of Empires")
AngryBirds= db.nodes.create(name="Angry Birds")
GunBound= db.nodes.create(name="Gun Bound")
#--------------------SIMULACION-------------------------
#4.1 simulacion de vehiculos
MarioKart= db.nodes.create(name="MarioKart") #carreras
NeedforSpeed= db.nodes.create(name="Need For Speed") #carreras
IronWarriors= db.nodes.create(name="Iron Warriors") 
#4.2 simulacion de construccion
MineCraft= db.nodes.create(name="Mine Craft")
ClashofClans= db.nodes.create(name="Clash of Clans")
GigiesSkylines= db.nodes.create(name="Gigies Skylines")
#----------------------DEPORTE--------------------------
#5.1 carreras
Fzero= db.nodes.create(name="F-Zero")
OutRun= db.nodes.create(name="Out Run")
ProyectCars= db.nodes.create(name="Proyect CARS")
#5.2 otros
FIFA= db.nodes.create(name="FIFA Series")
MarioStrikers= db.nodes.create(name="Mario Strikers")
WiiSports= db.nodes.create(name="WiiSports")
WiiFit= db.nodes.create(name="Wii Fit")
MarioySonic= db.nodes.create(name="Mario & Sonic en los juegos olimpicos")
#---------------------AVENTURA--------------------------
#6.1 accion-aventura
Zelda= db.nodes.create(name="The legend of Zelda")
TombRider= db.nodes.create(name="Tomb Rider")
GodofWar= db.nodes.create(name="God of war")
#6.2 survival horror
SilentHill= db.nodes.create(name="Silent Hill")
LastofUs= db.nodes.create(name="The last of Us")
ResidentEvil= db.nodes.create(name="Resident Evil")
#6.3 sigilo
AssassinsCreed= db.nodes.create(name="Assassins Creed")
MetalGear= db.nodes.create(name="MetalGear")
Dishonored= db.nodes.create(name="Dishonored")
#------------------------ROL----------------------------
StarWars= db.nodes.create(name="StarWars") #shooter, simulacion, aventura, accion
FinalFantasy= db.nodes.create(name="Final Fantasy")
Pokemon= db.nodes.create(name="Pokemon")
DungeonDragons= db.nodes.create(name="Dungeon & Dragons")
#---------------------SANDBOX---------------------------
WatchDogs= db.nodes.create(name="Watch Dogs") #sigilo, aventura
HorizonZero= db.nodes.create(name="Horizon Zero Dawn")
Prototype= db.nodes.create(name="Prototype")
#----------------------PUZZLE---------------------------
CandyCrush= db.nodes.create(name="Candy Crush")
Tetris= db.nodes.create(name="Tetris")
Portal= db.nodes.create(name="Portal")
Zuma= db.nodes.create(name="ZUMA")
QUBE= db.nodes.create(name="Q.U.B.E.")
#---------------------MUSICAL---------------------------
#10.1 karaoke
Lips= db.nodes.create(name="Lips")
SingIt= db.nodes.create(name="Sing it Disney")
#10.2 baile
DanceCentral= db.nodes.create(name="Dance Central")
JustDance= db.nodes.create(name="JustDance")
#10.3 instrumentos
GuitarHero= db.nodes.create(name="Guitar HERO")
DJHero= db.nodes.create(name="DJ HERO")
RockRevolution= db.nodes.create(name="Rock Revolution")

#***************************************************************************
#*************************Asignacion de Etiquetas***************************
#***************************************************************************
Caracteristica.add(Extrovertido,Introvertido,Atrevido)
Genero.add(Accion,Disparos,Estrategia,Simulacion,Deporte,Aventura,Rol,SandBox,Puzzle,Musical)

SubGenero.add(Lucha,Arcade,Plataformas,PraPersona,TraPersona,ShootemUp,TiempoReal,Turnos,Artilleria)
SubGenero.add(Vehiculos,Construccion,Carreras,AccionAventura,SurvivalHorror,Sigilo,Karaoke,Baile,Instrumentos)

VideoJuego.add(MortalCombat,SmashBros,DragonBall,PacMan,Contra,Sonic,Mario,MegaMan,DonkeyKong)
VideoJuego.add(Quake,Halo,CallofDuty,GrandTheft,GearsWar,DeadSpace,MetalSlug,SpaceInvaders,Rtype)
VideoJuego.add(AgeofEmpires,WarCraft,StarCraft,Civilization,EmpireTotalWar,AdvanceWars,Worms,AngryBirds,GunBound)
VideoJuego.add(MarioKart,NeedforSpeed,IronWarriors,MineCraft,ClashofClans,GigiesSkylines)
VideoJuego.add(Fzero,OutRun,ProyectCars,FIFA,MarioStrikers,WiiSports,WiiFit,MarioySonic)
VideoJuego.add(Zelda,TombRider,GodofWar,SilentHill,LastofUs,ResidentEvil,AssassinsCreed,MetalGear,Dishonored)
VideoJuego.add(StarWars,FinalFantasy,Pokemon,DungeonDragons,WatchDogs,HorizonZero,Prototype)
VideoJuego.add(CandyCrush,Tetris,Portal,Zuma,QUBE,Lips,SingIt,DanceCentral,JustDance,GuitarHero,DJHero,RockRevolution)

#***************************************************************************
#********************************Relaciones*********************************
#***************************************************************************
Extrovertido.relationships.create("G", Accion)
Extrovertido.relationships.create("G", Disparos)
Extrovertido.relationships.create("G", Estrategia)
Extrovertido.relationships.create("G", Simulacion)
Extrovertido.relationships.create("G", Aventura)
Extrovertido.relationships.create("G", Musical)
Introvertido.relationships.create("G", Estrategia)
Introvertido.relationships.create("G", Simulacion)
Introvertido.relationships.create("G", Deporte)
Introvertido.relationships.create("G", Rol)
Introvertido.relationships.create("G", Puzzle)
Introvertido.relationships.create("G", SandBox)
Atrevido.relationships.create("G", Accion)
Atrevido.relationships.create("G", Aventura)
Atrevido.relationships.create("G", Disparos)

#------------------------------------------------------------Accion
Accion.relationships.create("SubG", Lucha)
Lucha.relationships.create("VJ", MortalCombat)
Lucha.relationships.create("VJ",SmashBros)
AccionAventura.relationships.create("VJ", SmashBros)
Lucha.relationships.create("VJ",DragonBall)
AccionAventura.relationships.create("VJ", DragonBall)

Accion.relationships.create("SubG", Arcade)
Arcade.relationships.create("VJ", PacMan)
Arcade.relationships.create("VJ", Contra)
Plataformas.relationships.create("VJ", Contra)
AccionAventura.relationships.create("VJ", Contra)
ShootemUp.relationships.create("VJ", Contra)
Arcade.relationships.create("VJ", Sonic)
Plataformas.relationships.create("VJ", Sonic)

Accion.relationships.create("SubG", Plataformas)
Plataformas.relationships.create("VJ", Mario)
Plataformas.relationships.create("VJ", MegaMan)
AccionAventura.relationships.create("VJ", MegaMan)
ShootemUp.relationships.create("VJ", MegaMan)
Plataformas.relationships.create("VJ", DonkeyKong)
AccionAventura.relationships.create("VJ", DonkeyKong)
#----------------------------------------------------------Diparos
Disparos.relationships.create("SubG", PraPersona)
PraPersona.relationships.create("VJ", Quake)
AccionAventura.relationships.create("VJ", Quake)
PraPersona.relationships.create("VJ", Halo)
AccionAventura.relationships.create("VJ", Halo)
PraPersona.relationships.create("VJ", CallofDuty)
AccionAventura.relationships.create("VJ", CallofDuty)

Disparos.relationships.create("SubG", TraPersona)
TraPersona.relationships.create("VJ", GrandTheft)
TraPersona.relationships.create("VJ", GearsWar)
TraPersona.relationships.create("VJ", DeadSpace)

Disparos.relationships.create("SubG", ShootemUp)
ShootemUp.relationships.create("VJ", MetalSlug)
AccionAventura.relationships.create("VJ", MetalSlug)
ShootemUp.relationships.create("VJ", SpaceInvaders)
Arcade.relationships.create("VJ", SpaceInvaders)
ShootemUp.relationships.create("VJ", Rtype)
Vehiculos.relationships.create("VJ", Rtype)
AccionAventura.relationships.create("VJ", Rtype)
#----------------------------------------------------------Estrategia
Estrategia.relationships.create("SubG", TiempoReal)
TiempoReal.relationships.create("VJ", AgeofEmpires)
TiempoReal.relationships.create("VJ", StarCraft)
TiempoReal.relationships.create("VJ", WarCraft)

Estrategia.relationships.create("SubG", Turnos)
Turnos.relationships.create("VJ", Civilization)
Turnos.relationships.create("VJ", EmpireTotalWar)
Turnos.relationships.create("VJ", AdvanceWars)

Estrategia.relationships.create("SubG", Artilleria)
Artilleria.relationships.create("VJ", Worms)
ShootemUp.relationships.create("VJ", Worms)
Artilleria.relationships.create("VJ", AngryBirds)
TiempoReal.relationships.create("VJ", AngryBirds)
Artilleria.relationships.create("VJ", GunBound)
#----------------------------------------------------------Simulacion
Simulacion.relationships.create("SubG", Vehiculos)
Vehiculos.relationships.create("VJ", MarioKart)
Vehiculos.relationships.create("VJ", NeedforSpeed)
Vehiculos.relationships.create("VJ", IronWarriors)

Simulacion.relationships.create("SubG", Construccion)
Construccion.relationships.create("VJ", MineCraft)
Construccion.relationships.create("VJ", ClashofClans)
TiempoReal.relationships.create("VJ", ClashofClans)
SandBox.relationships.create("VJ", ClashofClans)
Construccion.relationships.create("VJ", GigiesSkylines)

#----------------------------------------------------------Deporte
Deporte.relationships.create("SubG", Carreras)
Deporte.relationships.create("VJ", FIFA)
Deporte.relationships.create("VJ", MarioStrikers)
Deporte.relationships.create("VJ", WiiSports)
Deporte.relationships.create("VJ", WiiFit)
Deporte.relationships.create("VJ", MarioySonic)
Carreras.relationships.create("VJ", Fzero)
Carreras.relationships.create("VJ", OutRun)
Carreras.relationships.create("VJ", ProyectCars)
#----------------------------------------------------------Aventura
Aventura.relationships.create("SubG", AccionAventura)
AccionAventura.relationships.create("VJ", Zelda)
AccionAventura.relationships.create("VJ", TombRider)
AccionAventura.relationships.create("VJ", GodofWar)
Lucha.relationships.create("VJ", GodofWar)

Aventura.relationships.create("SubG", SurvivalHorror)
SurvivalHorror.relationships.create("VJ", ResidentEvil)
SurvivalHorror.relationships.create("VJ", LastofUs)
SurvivalHorror.relationships.create("VJ", SilentHill)

Aventura.relationships.create("SubG", Sigilo)
Sigilo.relationships.create("VJ", AssassinsCreed)
AccionAventura.relationships.create("VJ", AssassinsCreed)
Sigilo.relationships.create("VJ", Dishonored)
AccionAventura.relationships.create("VJ", Dishonored)
Sigilo.relationships.create("VJ", MetalGear)
AccionAventura.relationships.create("VJ", MetalGear)
#----------------------------------------------------------Rol
Rol.relationships.create("VJ", StarWars)
AccionAventura.relationships.create("VJ", StarWars)
ShootemUp.relationships.create("VJ", StarWars)
Rol.relationships.create("VJ", FinalFantasy)
AccionAventura.relationships.create("VJ", FinalFantasy)
Rol.relationships.create("VJ", Pokemon)
Turnos.relationships.create("VJ", Pokemon)
Rol.relationships.create("VJ", DungeonDragons)
Arcade.relationships.create("VJ", DungeonDragons)
#----------------------------------------------------------SandBox
SandBox.relationships.create("VJ", WatchDogs)
AccionAventura.relationships.create("VJ", WatchDogs)
SandBox.relationships.create("VJ", HorizonZero)
Rol.relationships.create("VJ", HorizonZero)
SandBox.relationships.create("VJ", Prototype)
AccionAventura.relationships.create("VJ", Prototype)
#----------------------------------------------------------Puzzle
Puzzle.relationships.create("VJ", CandyCrush)
Puzzle.relationships.create("VJ", Tetris)
Puzzle.relationships.create("VJ", Portal)
Puzzle.relationships.create("VJ", Zuma)
Puzzle.relationships.create("VJ", QUBE)
#----------------------------------------------------------Musical
Musical.relationships.create("SubG", Karaoke)
Karaoke.relationships.create("VJ", Lips)
Karaoke.relationships.create("VJ", SingIt)

Musical.relationships.create("SubG", Baile)
Baile.relationships.create("VJ", JustDance)
Baile.relationships.create("VJ", DanceCentral)

Musical.relationships.create("SubG", Instrumentos)
Instrumentos.relationships.create("VJ", GuitarHero)
Instrumentos.relationships.create("VJ", DJHero)
Instrumentos.relationships.create("VJ", RockRevolution)



'''q = 'MATCH (u:caracteristica)-[r:a]->(m:regalo) WHERE u.name="Ropa" RETURN u, type(r), m'

results = db.query(q, returns=(client.Node, str, client.Node))
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))'''


