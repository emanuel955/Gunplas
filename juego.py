from random import randint, choice, uniform
from objetos import Gunpla, Esqueleto, Parte ,Arma, Pila, Cola

def main():
    cant_pilotos, cant_equipos, cupo_equipo = aleatorizador_de_pilotos_y_equipos()
    jugadores_equipos = repartir_pilotos(cant_equipos, cupo_equipo)
    partes, armas = aleatorizador_de_partes_y_armas(cant_pilotos)
    esqueletos = aleatorizador_de_esqueletos(cant_pilotos)
    partes_apiladas = apilar_lista(partes)
    armas_apiladas = apilar_lista(armas)
    elegir_esqueletos(jugadores_equipos, esqueletos)
    jugadores_encolados = encolar_lista(jugadores_equipos)
    repartir_armas_partes(jugadores_encolados,partes_apiladas,armas_apiladas)
    print (jugadores_equipos)




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
            jugadores_equipos.append(["Piloto " + str(piloto_del_equipo + 1), "Equipo " + str(numero_de_equipo + 1),[] ,[], [] ]) #Lista de personaje = [Nombre, Equipo, Esqueleto, Partes, Armas], es una lista para agregar mas cosas luego
    return jugadores_equipos

def aleatorizador_de_partes_y_armas(cant_pilotos):
    armas = []
    partes = []
    while len(armas) < (cant_pilotos * 6): #2 tipos de armas * 3 * pilotos (para que tengan para elegir)
        armas.append(crear_arma())
    while len(partes) < (cant_pilotos * 21): #7 tipos de partes * 3 * pilotos (para que tengan para elegir)
        partes.append(crear_parte())
    return partes, armas

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
    arma_presicion = round(uniform (0.0, 4.0),2) #Round redondea a dos decimales
    return Arma(arma_peso, arma_tipo, arma_clase, arma_municion, arma_velocidad, arma_armadura, arma_escudo, arma_energia, tiempo_de_recarga, arma_daño, arma_hits, arma_presicion)

def crear_parte():
    parte_tipo = choice(["CASCO","PECHO","HOMBROS","PIERNAS","BOTAS","GUANTES","ALAS"])
    if parte_tipo == "CASCO":
        parte_peso = randint(0, 75)
        parte_velocidad = randint(-20, 0)
        parte_slots_armas = randint (0,1)
        parte_armadura = randint(-20, 40)
        parte_escudo = randint(-20, 40)
        parte_energia = randint(-40, 30)
    if parte_tipo == "PECHO":
        parte_peso = randint(0, 110)
        parte_velocidad = randint(-50, 0)
        parte_slots_armas = 0
        parte_armadura = randint(-20, 50)
        parte_escudo = randint(-20, 50)
        parte_energia = randint(-60, 50)
    if parte_tipo == "HOMBROS":
        parte_peso = randint(0, 30)
        parte_velocidad = randint(-50, 0)
        parte_slots_armas = 0
        parte_armadura = randint(-20, 30)
        parte_escudo = randint(-20, 50)
        parte_energia = randint(-30, 30)
    if parte_tipo == "PIERNAS":
        parte_peso = randint(0, 90)
        parte_velocidad = randint(-50, 60)
        parte_slots_armas = 0
        parte_armadura = randint(-30, 60)
        parte_escudo = randint(-20, 50)
        parte_energia = randint(-40, 50)
    if parte_tipo == "BOTAS":
        parte_peso = randint(0, 50)
        parte_velocidad = randint(-30, 60)
        parte_slots_armas = 0
        parte_armadura = randint(-30, 25)
        parte_escudo = randint(-20, 20)
        parte_energia = randint(-20, 20)
    if parte_tipo == "GUANTES":
        parte_peso = randint(0, 20)
        parte_velocidad = randint(-30, 20)
        parte_slots_armas = randint(0,1)
        parte_armadura = randint(-10, 10)
        parte_escudo = randint(-10, 10)
        parte_energia = randint(-10, 10)
    if parte_tipo == "ALAS":
        parte_peso = randint(0, 75)
        parte_velocidad = randint(-50, 50)
        parte_slots_armas = randint(0,2)
        parte_armadura = randint(-25, 25)
        parte_escudo = randint(-60, 50)
        parte_energia = randint(-50, 50)
    if parte_slots_armas != 0:
        parte_armas_adosadas = []
        for i in range (parte_slots_armas):
            parte_armas_adosadas.append(crear_arma())
        return Parte(parte_peso, parte_armas_adosadas, parte_velocidad, parte_armadura, parte_escudo, parte_energia, parte_tipo)
    else:
        return Parte(parte_peso, 0, parte_velocidad, parte_armadura, parte_escudo, parte_energia, parte_tipo)

def aleatorizador_de_esqueletos(cant_pilotos):
    esqueletos = []
    for i in range (cant_pilotos * 3):
        esqueleto_energia = randint (1, 200)
        esqueleto_movilidad = randint (100, 300)
        esqueleto_velocidad = randint (0, 100)
        esqueleto_slot_armas = randint (0, 3)
        esqueletos.append(Esqueleto(esqueleto_energia,esqueleto_movilidad, esqueleto_slot_armas, esqueleto_velocidad))
    return esqueletos

def apilar_lista(lista):
    """Recibe una lista y la devuelve apilada"""
    nueva_pila = Pila()
    for item in lista:
        nueva_pila.apilar(item)
    return nueva_pila

def elegir_esqueletos(jugadores, esqueletos):
    for jugador in jugadores:
        jugador[2] = (choice(esqueletos))

def encolar_lista(lista):
    nueva_cola = Cola()
    for item in lista:
        nueva_cola.encolar(item)
    return nueva_cola

def repartir_armas_partes(jugadores_encolados,partes_apiladas,armas_apiladas):
    while partes_apiladas or armas_apiladas:
        jugador = jugadores_encolados.desencolar()
        if partes_apiladas and armas_apiladas:
            objeto_a_elegir = choice(["ARMAS", "PARTES"])
        elif not partes_apiladas:
            objeto_a_elegir = "ARMAS"
        elif not armas_apiladas:
            objeto_a_elegir = "PARTES"
        if objeto_a_elegir == "PARTES":
            jugador[3].append(partes_apiladas.desapilar())
        if objeto_a_elegir == "ARMAS":
            jugador[4].append(armas_apiladas.desapilar())
        jugadores_encolados.encolar(jugador)







main()
print()

