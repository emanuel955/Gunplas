from random import randint, choice
from objetos import Gunpla, Esqueleto, Parte ,Arma

def main():
    cant_pilotos, cant_equipos, cupo_equipo = aleatorizador_de_pilotos_y_equipos()
    jugadores_equipos = repartir_pilotos(cant_equipos, cupo_equipo)
    partes_y_armas = aleatorizador_de_partes_y_armas(cant_pilotos)







def es_primo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def aleatorizador_de_pilotos_y_equipos(): #La cantidad de pilotos debe ser si o si un numero no primo para poder dividirlos en grupos iguales
    cant_pilotos = randint(2,20)
    cant_equipos = randint(2, 5)
    cupo_equipo = int(cant_pilotos / cant_equipos)
    while es_primo(cant_pilotos) or (cant_pilotos % cant_equipos != 0):
        cant_pilotos = randint(2,20)
        cant_equipos = randint(2, 5)
        cupo_equipo = int(cant_pilotos / cant_equipos)
    print ("Cantidad de pilotos: ", cant_pilotos) #Prueba
    print ("Cantidad de equipos: ", cant_equipos) #Prueba
    print ("Cupo por equipo: ", cupo_equipo) #Prueba
    return cant_pilotos, cant_equipos, cupo_equipo

def repartir_pilotos(cant_equipos, cupo_equipo): #Posiciona los pilotos en sus respectivos equipos
    jugadores_equipos = []
    for numero_de_equipo in range (cant_equipos):
        for piloto_del_equipo in range (cupo_equipo):
            jugadores_equipos.append(["Piloto " + str(piloto_del_equipo + 1), "Equipo " + str(numero_de_equipo + 1)]) #Lista de personaje = [Nombre, Equipo], es una lista para agregar mas cosas luego
    print("Listado:\n", jugadores_equipos) #Prueba

def aleatorizador_de_partes_y_armas(cant_pilotos):
    armas = []
    partes = []
    while len(armas) < (cant_pilotos * 6):
        armas.append(crear_arma())


def crear_arma():
    tipo_arma = ["MELEE", "RANGO"]
    clases_melee = ["ESPADA", "DAGA", "MAZA", "HOZ", "PORRA", "BATE", "MARTILLO", "MOTOSIERRA", "KATANA", "LATIGO"]
    clases_rango = ["BALLESTA", "ARCO", "PISTOLA", "RIFLE", "LANZA", "HONDA", "ESCOPETA", "BOOMERANG"]
    municiones_arma = ["FISICA", "LASER", "HADRON"]
    arma_peso = randint(0, 100)
    arma_tipo = choice(tipo_arma)
    if arma_tipo == "MELEE":
        arma_clase = choice(clases_melee)
    if arma_tipo == "RANGO":
        arma_clase = choice(clases_rango)
    arma_municion = choice(municiones_arma)
    arma_velocidad = randint(-50,50)
    arma_armadura = randint(-50,50)
    arma_escudo = randint (-50,50)
    arma_energia = randint (-50,50)
    tiempo_de_recarga = randint (0,5)
    arma_daño = randint (1,50)
    arma_hits = randint (1,3)
    arma_presicion = randint (0,4) #preguntar por valores de presicion
    return Arma(arma_peso, arma_tipo, arma_clase, arma_municion, arma_velocidad, arma_armadura, arma_escudo, arma_energia, tiempo_de_recarga, arma_daño, arma_hits, arma_presicion)








main()
print()

