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
Habilidad = db.labels.create("Habilidad")
Edad = db.labels.create("Edad")
Genero = db.labels.create("Genero")
SubGenero = db.labels.create("Subgenero")
VideoJuego = db.labels.create("Videojuego")

#**********************Caracteristicas de la persona************************
Extrovertida= db.nodes.create(name="Extrovertida")
Introvertida= db.nodes.create(name="Introvertida")
Atrevida= db.nodes.create(name="Atrevida")
Creativa = db.nodes.create(name="Creativa")
Paciente = db.nodes.create(name="Paciente")

#************************Habilidades de la persona**************************
Logica = db.nodes.create(name="Logica")
Espacial = db.nodes.create(name="Espacial")
Motora = db.nodes.create(name="Motora")
MusicalRitmica = db.nodes.create(name="Musical-Ritmica")

#************************Rango de edad de la persona************************
Cinco_11 = db.nodes.create(name="4-11")
Doce_17 = db.nodes.create(name="12-17")
Dieciocho_70 = db.nodes.create(name="18-70")
TodasEdades = db.nodes.create(name="Todas las Edades")

#***************************************************************************
#******************************GENEROS**************************************
#***************************************************************************
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

#***************************************************************************
#****************************SUBGENEROS*************************************
#***************************************************************************
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
Vehiculos= db.nodes.create(name="Simu. Vehiculos")
Construccion= db.nodes.create(name="Simu. Construccion")
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

#***************************************************************************
#******************************VIDEOJUEGOS**********************************
#***************************************************************************
#-----------------------ACCION------------------------- #
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
Kirby = db.nodes.create(name="Kirby")
#----------------------DISPAROS------------------------ #
#2.1 primera persoa
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
#----------------------ESTRATEGIA----------------------- #
#3.1 estrategia en tiempo real
AgeofEmpires= db.nodes.create(name="Age Of Empires")
StarCraft= db.nodes.create(name="Star Craft")
WarCraft= db.nodes.create(name="War Craft")
#3.2 estrategia por turnos
Civilization= db.nodes.create(name="Civilization IV")
EmpireTotalWar= db.nodes.create(name="Empire Total War")
AdvanceWars= db.nodes.create(name="Advance Wars")
#3.3 artilleria
Worms= db.nodes.create(name="Worms")
AngryBirds= db.nodes.create(name="Angry Birds")
GunBound= db.nodes.create(name="Gun Bound")
#--------------------SIMULACION------------------------- #
#4.1 simulacion de vehiculos
MarioKart= db.nodes.create(name="MarioKart") #carreras
NeedforSpeed= db.nodes.create(name="Need For Speed") #carreras
IronWarriors= db.nodes.create(name="Iron Warriors")
Hawx = db.nodes.create(name="H.A.W.X.")
AssaultHorizon = db.nodes.create(name="Assault Horizon")
#4.2 simulacion de construccion
MineCraft= db.nodes.create(name="Mine Craft")
ClashofClans= db.nodes.create(name="Clash of Clans")
GigiesSkylines= db.nodes.create(name="Gigies Skylines")
Anno = db.nodes.create(name="ANNO")
SimCity = db.nodes.create(name="SimCity")
Banished= db.nodes.create(name="Banished")
#----------------------DEPORTE-------------------------- #
#5.1 carreras
Fzero= db.nodes.create(name="F-Zero")
OutRun= db.nodes.create(name="Out Run")
ProyectCars= db.nodes.create(name="Proyect CARS")
#5.2 otros
FIFA= db.nodes.create(name="FIFA Series")
MarioStrikers= db.nodes.create(name="Mario Strikers")
WiiSports= db.nodes.create(name="WiiSports")
WiiFit= db.nodes.create(name="Wii Fit")
MarioySonic= db.nodes.create(name="Mario & Sonic in the olimpyc games")
#---------------------AVENTURA-------------------------- #
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
#------------------------ROL---------------------------- #
StarWars= db.nodes.create(name="StarWars") #shooter, simulacion, aventura, accion
FinalFantasy= db.nodes.create(name="Final Fantasy")
Pokemon= db.nodes.create(name="Pokemon")
DungeonDragons= db.nodes.create(name="Dungeon & Dragons")
#---------------------SANDBOX--------------------------- #
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
Caracteristica.add(Extrovertida,Introvertida,Atrevida,Creativa,Paciente)
Habilidad.add(Logica,Espacial,Motora,MusicalRitmica)
Edad.add(Cinco_11,Doce_17,Dieciocho_70,TodasEdades)
Genero.add(Accion,Disparos,Estrategia,Simulacion,Deporte,Aventura,Rol,SandBox,Puzzle,Musical)

SubGenero.add(Lucha,Arcade,Plataformas,PraPersona,TraPersona,ShootemUp,TiempoReal,Turnos,Artilleria)
SubGenero.add(Vehiculos,Construccion,Carreras,AccionAventura,SurvivalHorror,Sigilo,Karaoke,Baile,Instrumentos)

VideoJuego.add(MortalCombat,SmashBros,DragonBall,PacMan,Contra,Sonic,Mario,MegaMan,DonkeyKong,Kirby)
VideoJuego.add(Quake,Halo,CallofDuty,GrandTheft,GearsWar,DeadSpace,MetalSlug,SpaceInvaders,Rtype)
VideoJuego.add(AgeofEmpires,WarCraft,StarCraft,Civilization,EmpireTotalWar,AdvanceWars,Worms,AngryBirds,GunBound)
VideoJuego.add(MarioKart,NeedforSpeed,IronWarriors,Hawx,AssaultHorizon,MineCraft,ClashofClans,GigiesSkylines,Anno,SimCity,Banished)
VideoJuego.add(Fzero,OutRun,ProyectCars,FIFA,MarioStrikers,WiiSports,WiiFit,MarioySonic)
VideoJuego.add(Zelda,TombRider,GodofWar,SilentHill,LastofUs,ResidentEvil,AssassinsCreed,MetalGear,Dishonored)
VideoJuego.add(StarWars,FinalFantasy,Pokemon,DungeonDragons,WatchDogs,HorizonZero,Prototype)
VideoJuego.add(CandyCrush,Tetris,Portal,Zuma,QUBE,Lips,SingIt,DanceCentral,JustDance,GuitarHero,DJHero,RockRevolution)

#***************************************************************************
#********************************Relaciones*********************************
#***************************************************************************

###########################CARACATERISTICAS#################################
#----------------------------Extrovertida-----------------------------------
Extrovertida.relationships.create("VJ",MortalCombat) #accion
Extrovertida.relationships.create("VJ",SmashBros)
Extrovertida.relationships.create("VJ",DragonBall)
Extrovertida.relationships.create("VJ",Contra)
Extrovertida.relationships.create("VJ",Sonic)
Extrovertida.relationships.create("VJ",PacMan)
Extrovertida.relationships.create("VJ",Mario)
Extrovertida.relationships.create("VJ",MegaMan)
Extrovertida.relationships.create("VJ",DonkeyKong)
Extrovertida.relationships.create("VJ",Kirby)

Extrovertida.relationships.create("VJ",Quake) #disparos
Extrovertida.relationships.create("VJ",Halo)
Extrovertida.relationships.create("VJ",CallofDuty)
Extrovertida.relationships.create("VJ",GrandTheft)
Extrovertida.relationships.create("VJ",GearsWar)
Extrovertida.relationships.create("VJ",DeadSpace)
Extrovertida.relationships.create("VJ",MetalSlug)
Extrovertida.relationships.create("VJ",SpaceInvaders)
Extrovertida.relationships.create("VJ",Rtype)

Extrovertida.relationships.create("VJ",AgeofEmpires) #Estrategia
Extrovertida.relationships.create("VJ",WarCraft)
Extrovertida.relationships.create("VJ",StarCraft)
Extrovertida.relationships.create("VJ",Civilization)
Extrovertida.relationships.create("VJ",EmpireTotalWar)
Extrovertida.relationships.create("VJ",AdvanceWars)
Extrovertida.relationships.create("VJ",Worms)
Extrovertida.relationships.create("VJ",AngryBirds)
Extrovertida.relationships.create("VJ",GunBound)

Extrovertida.relationships.create("VJ",MarioKart) #simulacion de vehiculos
Extrovertida.relationships.create("VJ",NeedforSpeed)
Extrovertida.relationships.create("VJ",IronWarriors)
Extrovertida.relationships.create("VJ",IronWarriors)
Extrovertida.relationships.create("VJ",Hawx)
Extrovertida.relationships.create("VJ",AssaultHorizon)

Extrovertida.relationships.create("VJ",Zelda) #aventura
Extrovertida.relationships.create("VJ",TombRider)
Extrovertida.relationships.create("VJ",GodofWar)
Extrovertida.relationships.create("VJ",SilentHill)
Extrovertida.relationships.create("VJ",LastofUs)
Extrovertida.relationships.create("VJ",ResidentEvil)
Extrovertida.relationships.create("VJ",AssassinsCreed)
Extrovertida.relationships.create("VJ",MetalGear)
Extrovertida.relationships.create("VJ",Dishonored)

Extrovertida.relationships.create("VJ",Lips) #musical
Extrovertida.relationships.create("VJ",SingIt)
Extrovertida.relationships.create("VJ",DanceCentral)
Extrovertida.relationships.create("VJ",JustDance)
Extrovertida.relationships.create("VJ",GuitarHero)
Extrovertida.relationships.create("VJ",DJHero)
Extrovertida.relationships.create("VJ",RockRevolution)

#----------------------------Introvertida-----------------------------------
Introvertida.relationships.create("VJ",AgeofEmpires) #Estrategia
Introvertida.relationships.create("VJ",WarCraft)
Introvertida.relationships.create("VJ",StarCraft)
Introvertida.relationships.create("VJ",Civilization)
Introvertida.relationships.create("VJ",EmpireTotalWar)
Introvertida.relationships.create("VJ",AdvanceWars)
Introvertida.relationships.create("VJ",Worms)
Introvertida.relationships.create("VJ",AngryBirds)
Introvertida.relationships.create("VJ",GunBound)

Introvertida.relationships.create("VJ",MineCraft) #simulacion de construccion
Introvertida.relationships.create("VJ",ClashofClans)
Introvertida.relationships.create("VJ",GigiesSkylines)
Introvertida.relationships.create("VJ",Anno)
Introvertida.relationships.create("VJ",SimCity)
Introvertida.relationships.create("VJ",Banished)

Introvertida.relationships.create("VJ",Fzero) #Deporte
Introvertida.relationships.create("VJ",OutRun)
Introvertida.relationships.create("VJ",ProyectCars)
Introvertida.relationships.create("VJ",FIFA)
Introvertida.relationships.create("VJ",MarioStrikers)
Introvertida.relationships.create("VJ",WiiSports)
Introvertida.relationships.create("VJ",WiiFit)
Introvertida.relationships.create("VJ",MarioySonic)

Introvertida.relationships.create("VJ",StarWars) #Rol
Introvertida.relationships.create("VJ",FinalFantasy)
Introvertida.relationships.create("VJ",Pokemon)
Introvertida.relationships.create("VJ",DungeonDragons)

Introvertida.relationships.create("VJ",CandyCrush) #Puzzle
Introvertida.relationships.create("VJ",Tetris)
Introvertida.relationships.create("VJ",Portal)
Introvertida.relationships.create("VJ",Zuma)
Introvertida.relationships.create("VJ",QUBE)

Introvertida.relationships.create("VJ",WatchDogs) #SandBox
Introvertida.relationships.create("VJ",HorizonZero)
Introvertida.relationships.create("VJ",Prototype)

#-----------------------------Atrevida---------------------------------------
Atrevida.relationships.create("VJ",MortalCombat) #accion
Atrevida.relationships.create("VJ",SmashBros)
Atrevida.relationships.create("VJ",DragonBall)
Atrevida.relationships.create("VJ",Contra)
Atrevida.relationships.create("VJ",Sonic)
Atrevida.relationships.create("VJ",PacMan)
Atrevida.relationships.create("VJ",Mario)
Atrevida.relationships.create("VJ",MegaMan)
Atrevida.relationships.create("VJ",DonkeyKong)
Atrevida.relationships.create("VJ",Kirby)

Atrevida.relationships.create("VJ",Quake) #disparos
Atrevida.relationships.create("VJ",Halo)
Atrevida.relationships.create("VJ",CallofDuty)
Atrevida.relationships.create("VJ",GrandTheft)
Atrevida.relationships.create("VJ",GearsWar)
Atrevida.relationships.create("VJ",DeadSpace)
Atrevida.relationships.create("VJ",MetalSlug)
Atrevida.relationships.create("VJ",SpaceInvaders)
Atrevida.relationships.create("VJ",Rtype)

Atrevida.relationships.create("VJ",Zelda) #aventura
Atrevida.relationships.create("VJ",TombRider)
Atrevida.relationships.create("VJ",GodofWar)
Atrevida.relationships.create("VJ",SilentHill)
Atrevida.relationships.create("VJ",LastofUs)
Atrevida.relationships.create("VJ",ResidentEvil)
Atrevida.relationships.create("VJ",AssassinsCreed)
Atrevida.relationships.create("VJ",MetalGear)
Atrevida.relationships.create("VJ",Dishonored)

#-------------------------------Creativa-------------------------------------
Creativa.relationships.create("VJ",CandyCrush) #Puzzle
Creativa.relationships.create("VJ",Tetris)
Creativa.relationships.create("VJ",Portal)
Creativa.relationships.create("VJ",Zuma)
Creativa.relationships.create("VJ",QUBE)

Creativa.relationships.create("VJ",WatchDogs) #SandBox
Creativa.relationships.create("VJ",HorizonZero)
Creativa.relationships.create("VJ",Prototype)

Creativa.relationships.create("VJ",MineCraft) #simulacion de construccion
Creativa.relationships.create("VJ",ClashofClans)
Creativa.relationships.create("VJ",GigiesSkylines)
Creativa.relationships.create("VJ",Anno)
Creativa.relationships.create("VJ",SimCity)
Creativa.relationships.create("VJ",Banished)

#-------------------------------Paciente-------------------------------------
Paciente.relationships.create("VJ",CandyCrush) #Puzzle
Paciente.relationships.create("VJ",Tetris)
Paciente.relationships.create("VJ",Portal)
Paciente.relationships.create("VJ",Zuma)
Paciente.relationships.create("VJ",QUBE)

Paciente.relationships.create("VJ",WatchDogs) #SandBox
Paciente.relationships.create("VJ",HorizonZero)
Paciente.relationships.create("VJ",Prototype)

Paciente.relationships.create("VJ",MineCraft) #simulacion de construccion
Paciente.relationships.create("VJ",ClashofClans)
Paciente.relationships.create("VJ",GigiesSkylines)
Paciente.relationships.create("VJ",Anno)
Paciente.relationships.create("VJ",SimCity)
Paciente.relationships.create("VJ",Banished)

Paciente.relationships.create("VJ",Zelda)
Paciente.relationships.create("VJ",AssassinsCreed)
Paciente.relationships.create("VJ",MetalGear)

##############################HABILIDADES####################################
#-------------------------------Logica---------------------------------------
Logica.relationships.create("VJ", GunBound) #puzzle
Logica.relationships.create("VJ",CandyCrush)
Logica.relationships.create("VJ",Tetris)
Logica.relationships.create("VJ",Portal)
Logica.relationships.create("VJ",Zuma)
Logica.relationships.create("VJ",QUBE)
Logica.relationships.create("VJ",WatchDogs) #SandBox
Logica.relationships.create("VJ",HorizonZero)
Logica.relationships.create("VJ",Prototype)

Logica.relationships.create("VJ", AngryBirds) #estrategia
Logica.relationships.create("VJ", Worms)
Logica.relationships.create("VJ", AgeofEmpires) 
Logica.relationships.create("VJ", StarCraft)
Logica.relationships.create("VJ", WarCraft)
Logica.relationships.create("VJ", ClashofClans)
Logica.relationships.create("VJ", Civilization)
Logica.relationships.create("VJ", EmpireTotalWar)
Logica.relationships.create("VJ", Pokemon)

#------------------------------Espacial--------------------------------------
Espacial.relationships.create("VJ",Zelda) #aventura
Espacial.relationships.create("VJ",TombRider)
Espacial.relationships.create("VJ",GodofWar)
Espacial.relationships.create("VJ",AssassinsCreed)
Espacial.relationships.create("VJ",MetalGear)
Espacial.relationships.create("VJ",Dishonored)
Espacial.relationships.create("VJ",Quake) #disparos
Espacial.relationships.create("VJ",Halo)
Espacial.relationships.create("VJ",CallofDuty)
Espacial.relationships.create("VJ",GrandTheft)
Espacial.relationships.create("VJ",GearsWar)
Espacial.relationships.create("VJ",DeadSpace)

Espacial.relationships.create("VJ", FIFA) #deporte
Espacial.relationships.create("VJ", MarioStrikers)
Espacial.relationships.create("VJ", WiiSports)
Espacial.relationships.create("VJ", WiiFit)
Espacial.relationships.create("VJ", MarioySonic)

#-------------------------------Motora---------------------------------------
Motora.relationships.create("VJ", JustDance) #musical
Motora.relationships.create("VJ", DanceCentral)
Motora.relationships.create("VJ", GuitarHero)
Motora.relationships.create("VJ", DJHero)
Motora.relationships.create("VJ", RockRevolution)
Motora.relationships.create("VJ", MortalCombat) #lucha
Motora.relationships.create("VJ", SmashBros)
Motora.relationships.create("VJ", DragonBall)
Motora.relationships.create("VJ", Quake) #disparos
Motora.relationships.create("VJ", Halo)
Motora.relationships.create("VJ", CallofDuty)

Motora.relationships.create("VJ", Fzero) #carreras
Motora.relationships.create("VJ", OutRun)
Motora.relationships.create("VJ", ProyectCars)
Motora.relationships.create("VJ", FIFA) #deporte
Motora.relationships.create("VJ", MarioStrikers)
Motora.relationships.create("VJ", WiiSports)
Motora.relationships.create("VJ", WiiFit)
Motora.relationships.create("VJ", MarioySonic)

Motora.relationships.create("VJ", MarioKart) #simulacion vehiculos
Motora.relationships.create("VJ", NeedforSpeed)
Motora.relationships.create("VJ", IronWarriors)
Motora.relationships.create("VJ", Hawx)
Motora.relationships.create("VJ", AssaultHorizon)

Motora.relationships.create("VJ",AssassinsCreed) #sigilo
Motora.relationships.create("VJ",MetalGear)
Motora.relationships.create("VJ",Dishonored)
#------------------------------MusicalRitmica---------------------------------------
MusicalRitmica.relationships.create("VJ", Lips) #musical
MusicalRitmica.relationships.create("VJ", SingIt)
MusicalRitmica.relationships.create("VJ", JustDance)
MusicalRitmica.relationships.create("VJ", DanceCentral)
MusicalRitmica.relationships.create("VJ", GuitarHero)
MusicalRitmica.relationships.create("VJ", DJHero)
MusicalRitmica.relationships.create("VJ", RockRevolution)
#################################EDAD########################################
#--------------------------------4-11----------------------------------------
Cinco_11.relationships.create("VJ", Mario)
Cinco_11.relationships.create("VJ", MegaMan)
Cinco_11.relationships.create("VJ", DonkeyKong)
Cinco_11.relationships.create("VJ", Kirby)
Cinco_11.relationships.create("VJ", Sonic)
Cinco_11.relationships.create("VJ", PacMan)
Cinco_11.relationships.create("VJ", MineCraft)
Cinco_11.relationships.create("VJ", MarioKart)
Cinco_11.relationships.create("VJ", Pokemon)

#--------------------------------12-17---------------------------------------
Doce_17.relationships.create("VJ", SpaceInvaders)
Doce_17.relationships.create("VJ", Contra)
Doce_17.relationships.create("VJ",SmashBros)
Doce_17.relationships.create("VJ",DragonBall)
Doce_17.relationships.create("VJ", Rtype)
Doce_17.relationships.create("VJ", Worms)
Doce_17.relationships.create("VJ", AngryBirds)
Doce_17.relationships.create("VJ", GunBound)                              
Doce_17.relationships.create("VJ", StarWars)
Doce_17.relationships.create("VJ", MetalSlug)
Doce_17.relationships.create("VJ", Rtype)
Doce_17.relationships.create("VJ", NeedforSpeed)
Doce_17.relationships.create("VJ", IronWarriors)
Doce_17.relationships.create("VJ", AssaultHorizon)
Doce_17.relationships.create("VJ", Hawx)

#--------------------------------18-70---------------------------------------
Dieciocho_70.relationships.create("VJ", GodofWar)
Dieciocho_70.relationships.create("VJ", DungeonDragons)
Dieciocho_70.relationships.create("VJ", MortalCombat)
Dieciocho_70.relationships.create("VJ", Quake)
Dieciocho_70.relationships.create("VJ", Halo)
Dieciocho_70.relationships.create("VJ", CallofDuty)
Dieciocho_70.relationships.create("VJ", GrandTheft)
Dieciocho_70.relationships.create("VJ", GearsWar)
Dieciocho_70.relationships.create("VJ", DeadSpace)

Dieciocho_70.relationships.create("VJ", AgeofEmpires)
Dieciocho_70.relationships.create("VJ", StarCraft)
Dieciocho_70.relationships.create("VJ", WarCraft)
Dieciocho_70.relationships.create("VJ", Civilization)
Dieciocho_70.relationships.create("VJ", EmpireTotalWar)
Dieciocho_70.relationships.create("VJ", AdvanceWars)

Dieciocho_70.relationships.create("VJ", GigiesSkylines)
Dieciocho_70.relationships.create("VJ", Anno)
Dieciocho_70.relationships.create("VJ", SimCity)
Dieciocho_70.relationships.create("VJ", Banished)

Dieciocho_70.relationships.create("VJ", Zelda)
Dieciocho_70.relationships.create("VJ", TombRider)
Dieciocho_70.relationships.create("VJ", GodofWar)

Dieciocho_70.relationships.create("VJ", SilentHill)
Dieciocho_70.relationships.create("VJ", LastofUs)
Dieciocho_70.relationships.create("VJ", ResidentEvil)

Dieciocho_70.relationships.create("VJ", AssassinsCreed)
Dieciocho_70.relationships.create("VJ", MetalGear)
Dieciocho_70.relationships.create("VJ", Dishonored)

Dieciocho_70.relationships.create("VJ", StarWars)
Dieciocho_70.relationships.create("VJ", FinalFantasy)
Dieciocho_70.relationships.create("VJ", DungeonDragons)

Dieciocho_70.relationships.create("VJ", WatchDogs)
Dieciocho_70.relationships.create("VJ", HorizonZero)
Dieciocho_70.relationships.create("VJ", Prototype)

#---------------------------Todas las edades-----------------------------------
TodasEdades.relationships.create("VJ", ClashofClans)

TodasEdades.relationships.create("VJ", Fzero)
TodasEdades.relationships.create("VJ", OutRun)
TodasEdades.relationships.create("VJ", ProyectCars)
TodasEdades.relationships.create("VJ", FIFA)
TodasEdades.relationships.create("VJ", MarioStrikers)
TodasEdades.relationships.create("VJ", WiiSports)
TodasEdades.relationships.create("VJ", WiiFit)
TodasEdades.relationships.create("VJ", MarioySonic)

TodasEdades.relationships.create("VJ", CandyCrush)
TodasEdades.relationships.create("VJ", Tetris)
TodasEdades.relationships.create("VJ", Portal)
TodasEdades.relationships.create("VJ", Zuma)
TodasEdades.relationships.create("VJ", QUBE)

TodasEdades.relationships.create("VJ", Lips)
TodasEdades.relationships.create("VJ", SingIt)
TodasEdades.relationships.create("VJ", DanceCentral)
TodasEdades.relationships.create("VJ", JustDance)
TodasEdades.relationships.create("VJ", GuitarHero)
TodasEdades.relationships.create("VJ", DJHero)
TodasEdades.relationships.create("VJ", RockRevolution)

################################GENERO#######################################
#-------------------------------Accion---------------------------------------
Accion.relationships.create("VJ", MortalCombat)
Accion.relationships.create("VJ",SmashBros)
Accion.relationships.create("VJ",DragonBall)
Accion.relationships.create("VJ", GodofWar)
Accion.relationships.create("VJ", PacMan)
Accion.relationships.create("VJ", SpaceInvaders)
Accion.relationships.create("VJ", DungeonDragons)
Accion.relationships.create("VJ", Mario)
Accion.relationships.create("VJ", MegaMan)
Accion.relationships.create("VJ", DonkeyKong)
Accion.relationships.create("VJ", Kirby)
Accion.relationships.create("VJ", Contra)
Accion.relationships.create("VJ", Sonic)
#------------------------------Disparos--------------------------------------
Disparos.relationships.create("VJ", Quake)
Disparos.relationships.create("VJ", Halo)
Disparos.relationships.create("VJ", CallofDuty)
Disparos.relationships.create("VJ", GrandTheft)
Disparos.relationships.create("VJ", GearsWar)
Disparos.relationships.create("VJ", DeadSpace)
Disparos.relationships.create("VJ", MetalSlug)
Disparos.relationships.create("VJ", SpaceInvaders)
Disparos.relationships.create("VJ", Rtype)
Disparos.relationships.create("VJ", Worms)
Disparos.relationships.create("VJ", StarWars)
#-----------------------------Estrategia-------------------------------------
Estrategia.relationships.create("VJ", AgeofEmpires)
Estrategia.relationships.create("VJ", StarCraft)
Estrategia.relationships.create("VJ", WarCraft)
Estrategia.relationships.create("VJ", ClashofClans)
Estrategia.relationships.create("VJ", Civilization)
Estrategia.relationships.create("VJ", EmpireTotalWar)
Estrategia.relationships.create("VJ", AdvanceWars)
Estrategia.relationships.create("VJ", AngryBirds)
Estrategia.relationships.create("VJ", Pokemon)
#-----------------------------Simulacion-------------------------------------
Simulacion.relationships.create("VJ", Rtype)
Simulacion.relationships.create("VJ", MarioKart)
Simulacion.relationships.create("VJ", NeedforSpeed)
Simulacion.relationships.create("VJ", IronWarriors)
Simulacion.relationships.create("VJ", Hawx)
Simulacion.relationships.create("VJ", AssaultHorizon)
Simulacion.relationships.create("VJ", MineCraft)
Simulacion.relationships.create("VJ", ClashofClans)
Simulacion.relationships.create("VJ", GigiesSkylines)
Simulacion.relationships.create("VJ", Anno)
Simulacion.relationships.create("VJ", SimCity)
Simulacion.relationships.create("VJ", Banished)
#--------------------------------Deporte-------------------------------------
Deporte.relationships.create("SubG", Carreras)
Deporte.relationships.create("VJ", FIFA)
Deporte.relationships.create("VJ", MarioStrikers)
Deporte.relationships.create("VJ", WiiSports)
Deporte.relationships.create("VJ", WiiFit)
Deporte.relationships.create("VJ", MarioySonic)
#-------------------------------Aventura-------------------------------------
Aventura.relationships.create("VJ", SmashBros)
Aventura.relationships.create("VJ", DragonBall)
Aventura.relationships.create("VJ", Contra)
Aventura.relationships.create("VJ", Sonic)
Aventura.relationships.create("VJ", MegaMan)
Aventura.relationships.create("VJ", DonkeyKong)
Aventura.relationships.create("VJ", Quake)
Aventura.relationships.create("VJ", Halo)
Aventura.relationships.create("VJ", CallofDuty)
Aventura.relationships.create("VJ", MetalSlug)
Aventura.relationships.create("VJ", Rtype)
Aventura.relationships.create("VJ", Zelda)
Aventura.relationships.create("VJ", TombRider)
Aventura.relationships.create("VJ", GodofWar)
Aventura.relationships.create("VJ", AssassinsCreed)
Aventura.relationships.create("VJ", Dishonored)
Aventura.relationships.create("VJ", MetalGear)
Aventura.relationships.create("VJ", StarWars)
Aventura.relationships.create("VJ", FinalFantasy)
Aventura.relationships.create("VJ", Prototype)
Aventura.relationships.create("VJ", WatchDogs)
Aventura.relationships.create("VJ", ResidentEvil)
Aventura.relationships.create("VJ", LastofUs)
Aventura.relationships.create("VJ", SilentHill)
Aventura.relationships.create("VJ", AssassinsCreed)
Aventura.relationships.create("VJ", Dishonored)
Aventura.relationships.create("VJ", MetalGear)
#------------------------------------Rol-------------------------------------
Rol.relationships.create("VJ", StarWars)
Rol.relationships.create("VJ", FinalFantasy)
Rol.relationships.create("VJ", Pokemon)
Rol.relationships.create("VJ", DungeonDragons)
Rol.relationships.create("VJ", HorizonZero)
#--------------------------------SandBox-------------------------------------
SandBox.relationships.create("VJ", ClashofClans)
SandBox.relationships.create("VJ", WatchDogs)
SandBox.relationships.create("VJ", HorizonZero)
SandBox.relationships.create("VJ", Prototype)
#---------------------------------Puzzle-------------------------------------
Puzzle.relationships.create("VJ", CandyCrush)
Puzzle.relationships.create("VJ", Tetris)
Puzzle.relationships.create("VJ", Portal)
Puzzle.relationships.create("VJ", Zuma)
Puzzle.relationships.create("VJ", QUBE)
#--------------------------------Musical-------------------------------------
Musical.relationships.create("VJ", Lips)
Musical.relationships.create("VJ", SingIt)
Musical.relationships.create("VJ", JustDance)
Musical.relationships.create("VJ", DanceCentral)
Musical.relationships.create("VJ", GuitarHero)
Musical.relationships.create("VJ", DJHero)
Musical.relationships.create("VJ", RockRevolution)
###############################SUBGENERO#####################################
#-------------------------------Lucha----------------------------------------
Lucha.relationships.create("VJ", MortalCombat)
Lucha.relationships.create("VJ",SmashBros)
Lucha.relationships.create("VJ",DragonBall)
Lucha.relationships.create("VJ", GodofWar)
#------------------------------Arcade----------------------------------------
Arcade.relationships.create("VJ", PacMan)
Arcade.relationships.create("VJ", Contra)
Arcade.relationships.create("VJ", Sonic)
Arcade.relationships.create("VJ", SpaceInvaders)
Arcade.relationships.create("VJ", DungeonDragons)
#-------------------------------Plataformas----------------------------------
Plataformas.relationships.create("VJ", Mario)
Plataformas.relationships.create("VJ", MegaMan)
Plataformas.relationships.create("VJ", DonkeyKong)
Plataformas.relationships.create("VJ", Kirby)
Plataformas.relationships.create("VJ", Contra)
Plataformas.relationships.create("VJ", Sonic)
#------------------------------Disp 1ra persona------------------------------
PraPersona.relationships.create("VJ", Quake)
PraPersona.relationships.create("VJ", Halo)
PraPersona.relationships.create("VJ", CallofDuty)
#------------------------------Disp 3ra persona------------------------------
TraPersona.relationships.create("VJ", GrandTheft)
TraPersona.relationships.create("VJ", GearsWar)
TraPersona.relationships.create("VJ", DeadSpace)
#------------------------------Shootemup-------------------------------------
ShootemUp.relationships.create("VJ", MetalSlug)
ShootemUp.relationships.create("VJ", SpaceInvaders)
ShootemUp.relationships.create("VJ", Rtype)
ShootemUp.relationships.create("VJ", Worms)
ShootemUp.relationships.create("VJ", StarWars)
#-------------------------------Estrategia Treal-----------------------------
TiempoReal.relationships.create("VJ", AgeofEmpires)
TiempoReal.relationships.create("VJ", StarCraft)
TiempoReal.relationships.create("VJ", WarCraft)
TiempoReal.relationships.create("VJ", ClashofClans)
#------------------------------Estrateiga Turnos-----------------------------
Turnos.relationships.create("VJ", Civilization)
Turnos.relationships.create("VJ", EmpireTotalWar)
Turnos.relationships.create("VJ", AdvanceWars)
Turnos.relationships.create("VJ", AngryBirds)
Turnos.relationships.create("VJ", Pokemon)
#-------------------------------Artilleria-----------------------------------
Artilleria.relationships.create("VJ", Worms)
Artilleria.relationships.create("VJ", AngryBirds)
Artilleria.relationships.create("VJ", GunBound)
#------------------------------Simulacion Vehiculos--------------------------
Vehiculos.relationships.create("VJ", Rtype)
Vehiculos.relationships.create("VJ", MarioKart)
Vehiculos.relationships.create("VJ", NeedforSpeed)
Vehiculos.relationships.create("VJ", IronWarriors)
Vehiculos.relationships.create("VJ", Hawx)
Vehiculos.relationships.create("VJ", AssaultHorizon)
#-------------------------------Simulacion construccion----------------------
Construccion.relationships.create("VJ", MineCraft)
Construccion.relationships.create("VJ", ClashofClans)
Construccion.relationships.create("VJ", GigiesSkylines)
Construccion.relationships.create("VJ", Anno)
Construccion.relationships.create("VJ", SimCity)
Construccion.relationships.create("VJ", Banished)
#------------------------------Carreras--------------------------------------
Carreras.relationships.create("VJ", Fzero)
Carreras.relationships.create("VJ", OutRun)
Carreras.relationships.create("VJ", ProyectCars)
#-------------------------------Accion Aventura------------------------------
AccionAventura.relationships.create("VJ", SmashBros)
AccionAventura.relationships.create("VJ", DragonBall)
AccionAventura.relationships.create("VJ", Contra)
AccionAventura.relationships.create("VJ", Sonic)
AccionAventura.relationships.create("VJ", MegaMan)
AccionAventura.relationships.create("VJ", DonkeyKong)
AccionAventura.relationships.create("VJ", Quake)
AccionAventura.relationships.create("VJ", Halo)
AccionAventura.relationships.create("VJ", CallofDuty)
AccionAventura.relationships.create("VJ", MetalSlug)
AccionAventura.relationships.create("VJ", Rtype)
AccionAventura.relationships.create("VJ", Zelda)
AccionAventura.relationships.create("VJ", TombRider)
AccionAventura.relationships.create("VJ", GodofWar)
AccionAventura.relationships.create("VJ", AssassinsCreed)
AccionAventura.relationships.create("VJ", Dishonored)
AccionAventura.relationships.create("VJ", MetalGear)
AccionAventura.relationships.create("VJ", StarWars)
AccionAventura.relationships.create("VJ", FinalFantasy)
AccionAventura.relationships.create("VJ", Prototype)
AccionAventura.relationships.create("VJ", WatchDogs)
#------------------------------SurvivalHorror--------------------------------
SurvivalHorror.relationships.create("VJ", ResidentEvil)
SurvivalHorror.relationships.create("VJ", LastofUs)
SurvivalHorror.relationships.create("VJ", SilentHill)
#-------------------------------Sigilo---------------------------------------
Sigilo.relationships.create("VJ", AssassinsCreed)
Sigilo.relationships.create("VJ", Dishonored)
Sigilo.relationships.create("VJ", MetalGear)
#------------------------------karaoke---------------------------------------
Karaoke.relationships.create("VJ", Lips)
Karaoke.relationships.create("VJ", SingIt)
#------------------------------Baile---------------------------------------
Baile.relationships.create("VJ", JustDance)
Baile.relationships.create("VJ", DanceCentral)
#-----------------------------Instrumentos---------------------------------------
Instrumentos.relationships.create("VJ", GuitarHero)
Instrumentos.relationships.create("VJ", DJHero)
Instrumentos.relationships.create("VJ", RockRevolution)



###############################################################################################
###############################################################################################
###############################################################################################



