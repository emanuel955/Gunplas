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
    elegir_partes(jugadores_encolados)
    elegir_armas(jugadores_encolados)
    gunplas_encolados = fabricar_gunpla(jugadores_encolados)
    # encolar_por_velocidad(gunplas_encolados)
    prueba = gunplas_encolados.desencolar()
    # print (prueba)
    print (prueba[2].get_movilidad())


def es_primo(num):
    """Recibe un numero y devuelve si es primo o no"""
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def aleatorizador_de_pilotos_y_equipos(): #La cantidad de pilotos debe ser si o si un numero no primo para poder dividirlos en grupos iguales
    """Elige aleatoriamente una cantidad de pilotos (Maximo 20, minimo 2) y los divide en grupos iguales (maximo 5), luego, devuelve la cantidad de pilotos, equipos y el cupo de pilotos por equipo"""
    cant_pilotos = randint(2,20)
    cant_equipos = randint(2, 5)
    cupo_equipo = int(cant_pilotos / cant_equipos)
    while es_primo(cant_pilotos) or (cant_pilotos % cant_equipos != 0):
        cant_pilotos = randint(2,20)
        cant_equipos = randint(2, 5)
        cupo_equipo = int(cant_pilotos / cant_equipos)
    # print ("Cantidad de pilotos: ", cant_pilotos) #Prueba
    # print ("Cantidad de equipos: ", cant_equipos) #Prueba
    # print ("Cupo por equipo: ", cupo_equipo) #Prueba
    return cant_pilotos, cant_equipos, cupo_equipo

def repartir_pilotos(cant_equipos, cupo_equipo):
    """Recibe la cantidad de equipos y el cupo de cada uno y reparte los pilotos en cada grupo, luego, los mezcla en una lista y la devuelve"""
    jugadores_equipos = []
    for numero_de_equipo in range (cant_equipos):
        for piloto_del_equipo in range (cupo_equipo):
            jugadores_equipos.append(["Piloto " + str(piloto_del_equipo + 1), "Equipo " + str(numero_de_equipo + 1),[] ,[], [] ]) #Lista de personaje = [Nombre, Equipo, Esqueleto, Partes, Armas], es una lista para agregar mas cosas luego
    jugadores_equipos_mezclados = mezclar_lista(jugadores_equipos)
    return jugadores_equipos_mezclados

def mezclar_lista(lista):
    """Recibe una lista y la devuelve mezclada, en una lista nueva"""
    lista_nueva = []
    while lista:
        item = choice(lista)
        lista.remove(item)
        lista_nueva.append(item)
    return lista_nueva

def aleatorizador_de_partes_y_armas(cant_pilotos):
    """Recibe la cantidad de pilotos y, dependiendo de esta, crea una cantidad determinada de armas y partes para que estos tengan varias para elegir, los devuelve en dos listas de Objetos"""
    armas = []
    partes = []
    while len(armas) < (cant_pilotos * 6): #2 tipos de armas * 3 * pilotos (para que tengan para elegir)
        armas.append(crear_arma())
    while len(partes) < (cant_pilotos * 21): #7 tipos de partes * 3 * pilotos (para que tengan para elegir)
        partes.append(crear_parte())
    return partes, armas

def crear_arma():
    """Crea un arma aleatoria y la devuelve como objeto"""
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
    arma_energia = randint (-100,300)
    tiempo_de_recarga = randint (0,5)
    arma_daño = randint (1,50)
    arma_hits = randint (1,3)
    arma_presicion = round(uniform (0.0, 4.0),2) #Round redondea a dos decimales
    return Arma(arma_peso, arma_tipo, arma_clase, arma_municion, arma_velocidad, arma_armadura, arma_escudo, arma_energia, tiempo_de_recarga, arma_daño, arma_hits, arma_presicion)

def crear_parte():
    """Crea una parte aleatoria y la devuelve como objeto"""
    parte_tipo = choice(["CASCO","PECHO","HOMBROS","PIERNAS","BOTAS","GUANTES","ALAS"])
    if parte_tipo == "CASCO":
        parte_peso = randint(0, 75)
        parte_velocidad = randint(-20, 0)
        parte_slots_armas = randint (0,1)
        parte_armadura = randint(-20, 40)
        parte_escudo = randint(-20, 40)
        parte_energia = randint(-100, 300)
    if parte_tipo == "PECHO":
        parte_peso = randint(0, 110)
        parte_velocidad = randint(-50, 0)
        parte_slots_armas = 0
        parte_armadura = randint(-20, 50)
        parte_escudo = randint(-20, 50)
        parte_energia = randint(-100,400)
    if parte_tipo == "HOMBROS":
        parte_peso = randint(0, 30)
        parte_velocidad = randint(-50, 0)
        parte_slots_armas = 0
        parte_armadura = randint(-20, 30)
        parte_escudo = randint(-20, 50)
        parte_energia = randint(-100, 150)
    if parte_tipo == "PIERNAS":
        parte_peso = randint(0, 90)
        parte_velocidad = randint(-50, 60)
        parte_slots_armas = 0
        parte_armadura = randint(-30, 60)
        parte_escudo = randint(-20, 50)
        parte_energia = randint(-100,350)
    if parte_tipo == "BOTAS":
        parte_peso = randint(0, 50)
        parte_velocidad = randint(-30, 60)
        parte_slots_armas = 0
        parte_armadura = randint(-30, 25)
        parte_escudo = randint(-20, 20)
        parte_energia = randint(-100,200)
    if parte_tipo == "GUANTES":
        parte_peso = randint(0, 20)
        parte_velocidad = randint(-30, 20)
        parte_slots_armas = randint(0,1)
        parte_armadura = randint(-10, 10)
        parte_escudo = randint(-10, 10)
        parte_energia = randint(-100,150)
    if parte_tipo == "ALAS":
        parte_peso = randint(0, 75)
        parte_velocidad = randint(-50, 50)
        parte_slots_armas = randint(0,2)
        parte_armadura = randint(-25, 25)
        parte_escudo = randint(-60, 50)
        parte_energia = randint(-100, 50)
    if parte_slots_armas != 0:
        parte_armas_adosadas = []
        for i in range (parte_slots_armas):
            parte_armas_adosadas.append(crear_arma())
        return Parte(parte_peso, parte_armas_adosadas, parte_velocidad, parte_armadura, parte_escudo, parte_energia, parte_tipo)
    else:
        return Parte(parte_peso, 0, parte_velocidad, parte_armadura, parte_escudo, parte_energia, parte_tipo)

def aleatorizador_de_esqueletos(cant_pilotos):
    """Recibe la cantidad de pilotos y, dependiendo de esta, crea una cantidad de esqueletos de caracteristicas aleatorias para que tengan para elegir, los devuelve dentro de una lista de objetos"""
    esqueletos = []
    for i in range (cant_pilotos * 3):
        esqueleto_energia = randint (1, 1000)
        esqueleto_movilidad = randint (100, 300)
        esqueleto_velocidad = randint (200,400)
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
    """Recibe la lista de jugadores y la de esqueletos y hace que estos los elijan aleatoriamente"""
    for jugador in jugadores:
        jugador[2] = (choice(esqueletos))

def encolar_lista(lista):
    """Recibe una lista y la devuelve encolada"""
    nueva_cola = Cola()
    for item in lista:
        nueva_cola.encolar(item)
    return nueva_cola

def repartir_armas_partes(jugadores_encolados,partes_apiladas,armas_apiladas):
    """Recibe la cola de jugadores, la lista de partes y la de armas, luego hace que estos en su turno recojan aleatoriamente (la agreguen a la lista de personajes y sus caracteristicas) un arma o parte que este en el tope de su respectiva fila, los jugadores se vuelven a encolar hasta que ambas listas queden vacias"""
    while not partes_apiladas.esta_vacia() or not armas_apiladas.esta_vacia():
        jugador = jugadores_encolados.desencolar()
        if partes_apiladas.esta_vacia():
            objeto_a_elegir = "ARMAS"
        elif armas_apiladas.esta_vacia():
            objeto_a_elegir = "PARTES"
        else:
            objeto_a_elegir = choice(["ARMAS", "PARTES"])
        if objeto_a_elegir == "PARTES":
            jugador[3].append(partes_apiladas.desapilar())
        if objeto_a_elegir == "ARMAS":
            jugador[4].append(armas_apiladas.desapilar())
        jugadores_encolados.encolar(jugador)

def elegir_partes(jugadores_encolados):
    """Recibe la cola de jugadores y a cada uno lo hace quedarse con una parte de cada tipo, si es que cuentan con todos los tipos de armas, y las demas son desechadas"""
    cola_aux = Cola()
    while not jugadores_encolados.esta_vacia():
        lista_aux = []
        lista_aux_tipos = []
        jugador = jugadores_encolados.desencolar()
        cola_aux.encolar(jugador)
        while (not "CASCO" in lista_aux) or (not "PECHO" in lista_aux) or (not "HOMBROS" in lista_aux) or (not "PIERNAS" in lista_aux) or (not "BOTAS" in lista_aux) or (not "GUANTES" in lista_aux) or (not "ALAS" in lista_aux):
            aux = choice(jugador[3])
            jugador[3].remove(aux)
            if aux.get_tipo_parte() not in lista_aux_tipos:
                lista_aux_tipos.append(aux.get_tipo_parte())
                lista_aux.append(aux)
            if not jugador[3]:
                break
        jugador[3] = lista_aux
    while not cola_aux.esta_vacia():
        jugadores_encolados.encolar(cola_aux.desencolar())

def elegir_armas(jugadores_encolados):
    """Recibe la cola de jugadores y se equipa aleatoriamente con las armas que le entren al esqueleto del gunpla, las armas sobrantes son desechadas"""
    cola_aux = Cola()
    while not jugadores_encolados.esta_vacia():
        lista_aux = []
        jugador = jugadores_encolados.desencolar()
        cola_aux.encolar(jugador)
        for i in range (jugador[2].get_cantidad_slots()):
            aux = choice(jugador[4])
            jugador[4].remove(aux)
            lista_aux.append(aux)
        jugador[4] = lista_aux
    while not cola_aux.esta_vacia():
        jugadores_encolados.encolar(cola_aux.desencolar())

def fabricar_gunpla(jugadores_encolados):
    nueva_cola = Cola()
    while not jugadores_encolados.esta_vacia():
        jugador = jugadores_encolados.desencolar()
        gunpla_fabricado = Gunpla(jugador[2],jugador[3],jugador[4])
        nueva_cola.encolar([jugador[0],jugador[1],gunpla_fabricado])
    return nueva_cola








main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()
main()
print()

