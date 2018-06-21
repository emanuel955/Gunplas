from random import randint, choice, uniform
from objetos import Gunpla, Esqueleto, Parte ,Arma, Pila, Cola, Piloto
from time import sleep
from time import strftime

def main():
    cant_pilotos, cant_equipos, cupo_equipo = aleatorizador_de_pilotos_y_equipos()
    print(strftime("[%H:%M:%S]:"),"La batalla se llevara a cabo entre",cant_equipos,"con",cupo_equipo,"pilotos cada uno")
    print(strftime("[%H:%M:%S]:"))
    jugadores_equipos = repartir_pilotos(cant_equipos, cupo_equipo)
    partes, armas = aleatorizador_de_partes_y_armas(cant_pilotos)
    esqueletos = aleatorizador_de_esqueletos(cant_pilotos)
    partes_apiladas = apilar_lista(partes)
    armas_apiladas = apilar_lista(armas)
    sleep(0.5)
    print(strftime("[%H:%M:%S]:"),"Hora de elegir los esqueletos!")
    print(strftime("[%H:%M:%S]:"))
    elegir_esqueletos(jugadores_equipos, esqueletos)
    sleep(0.5)
    print(strftime("[%H:%M:%S]:"))
    jugadores_encolados = encolar_lista(jugadores_equipos)
    repartir_armas_partes(jugadores_encolados,partes_apiladas,armas_apiladas)
    elegir_partes(jugadores_encolados)
    elegir_armas(jugadores_encolados)
    gunplas_encolados = gunpla_por_velocidad(jugadores_encolados)
    iniciar_batalla(gunplas_encolados, cant_equipos, cant_pilotos)


def es_primo(num):
    """Recibe un numero y devuelve si es primo o no"""
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def quick_sort_velocidad(lista):
    """Ordena la lista de forma recursiva.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada. """
    _quick_sort(lista, 0, len(lista) - 1)

def _quick_sort(lista, inicio, fin):
    """Función quick_sort recursiva.
    Pre: los índices inicio y fin indican sobre qué porción operar.
    Post: la lista está ordenada."""
    if inicio >= fin:
        return
    menores = _partition(lista, inicio, fin)
    _quick_sort(lista, inicio, menores - 1)
    _quick_sort(lista, menores + 1, fin)

def _partition(lista, inicio, fin):
    """Función partición que trabaja sobre la misma lista.
    Pre: los índices inicio y fin indican sobre qué porción operar.
    Post: los menores están antes que el pivote, los mayores después.
    Devuelve: la posición en la que quedó ubicado el pivote."""
    pivote = lista[inicio][0].get_gunpla().get_velocidad()
    menores = inicio
    # Ubicar menores a la izquierda, mayores a la derecha
    for i in range(inicio + 1, fin + 1):
        if lista[i][0].get_gunpla().get_velocidad() < pivote:
            menores += 1
            if i != menores:
                _swap(lista, i, menores)
        # Ubicar el pivote al final de los menores
    if inicio != menores:
        _swap(lista, inicio, menores)
    return menores

def _swap(lista, i, j):
    """Intercambia los elementos i y j de lista."""
    lista[j], lista[i] = lista[i], lista[j]

def enlistar_cola(cola):
    '''recibe una cola y devuelve una lista con sus datos en el mismo orden'''
    nueva_lista = []
    while not cola.esta_vacia():
        aux = cola.desencolar()
        nueva_lista.append(aux)
    for item in nueva_lista:
        cola.encolar(item)
    return nueva_lista

def aleatorizador_de_pilotos_y_equipos(): #La cantidad de pilotos debe ser si o si un numero no primo para poder dividirlos en grupos iguales
    """Elige aleatoriamente una cantidad de pilotos (Maximo 20, minimo 2) y los divide en grupos iguales (maximo 5), luego, devuelve la cantidad de pilotos, equipos y el cupo de pilotos por equipo"""
    cant_pilotos = randint(2,20)
    cant_equipos = randint(2, 5)
    cupo_equipo = int(cant_pilotos / cant_equipos)
    while es_primo(cant_pilotos) or (cant_pilotos % cant_equipos != 0):
        cant_pilotos = randint(2,20)
        cant_equipos = randint(2, 5)
        cupo_equipo = int(cant_pilotos / cant_equipos)
    return cant_pilotos, cant_equipos, cupo_equipo

def repartir_pilotos(cant_equipos, cupo_equipo):
    """Recibe la cantidad de equipos y el cupo de cada uno y reparte los pilotos en cada grupo, luego, los mezcla en una lista y la devuelve"""
    jugadores_equipos = []
    for numero_de_equipo in range (cant_equipos):
        for piloto_del_equipo in range (cupo_equipo):
            jugadores_equipos.append([Piloto("Jugador " + str(piloto_del_equipo + 1)), "Equipo " + str(numero_de_equipo + 1),[] ,{"CASCO" : [],"PECHO" : [],"HOMBROS" : [],"PIERNAS" : [],"BOTAS" : [],"GUANTES" : [],"ALAS" : []}, [] ]) #Lista de personaje = [Nombre, Equipo, Esqueleto, Partes, Armas], es una lista para agregar mas cosas luego
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
    while len(armas) < (cant_pilotos * 14):
        armas.append(crear_arma())
    while len(partes) < (cant_pilotos * 42):
        partes.append(crear_parte())
    return partes, armas

def crear_arma():
    """Crea un arma aleatoria y la devuelve como objeto"""
    tipo_arma = ["MELEE", "RANGO"]
    clases_melee = ["ESPADA", "DAGA", "MAZA", "HOZ", "PORRA", "BATE", "MARTILLO", "MOTOSIERRA", "KATANA", "LATIGO"]
    clases_rango = ["BALLESTA", "ARCO", "PISTOLA", "RIFLE", "LANZA", "HONDA", "ESCOPETA", "BOOMERANG"]
    municiones_arma = ["FISICA", "LASER", "HADRON"]
    arma_peso = randint(0, 10)
    arma_tipo = choice(tipo_arma)
    if arma_tipo == "MELEE":
        arma_clase = choice(clases_melee)
    if arma_tipo == "RANGO":
        arma_clase = choice(clases_rango)
    arma_municion = choice(municiones_arma)
    arma_velocidad = randint(-20,50)
    arma_armadura = randint(-50,50)
    arma_escudo = randint (-50,50)
    arma_energia = randint (-100,300)
    tiempo_de_recarga = randint (0,5)
    arma_dano = randint (1,50)
    arma_hits = randint (1,3)
    arma_presicion = round(uniform (0.0, 4.0),2) #Round redondea a dos decimales
    return Arma(arma_peso, arma_tipo, arma_clase, arma_municion, arma_velocidad, arma_armadura, arma_escudo, arma_energia, tiempo_de_recarga, arma_dano, arma_hits, arma_presicion)

def crear_parte():
    """Crea una parte aleatoria y la devuelve como objeto"""
    parte_tipo = choice(["CASCO", "PECHO", "HOMBROS", "PIERNAS", "BOTAS", "GUANTES", "ALAS"])
    if parte_tipo == "CASCO":
        parte_peso = randint(0, 10)
        parte_velocidad = randint(-5, 0)
        parte_slots_armas = randint (0,1)
        parte_armadura = randint(-20, 40)
        parte_escudo = randint(-20, 40)
        parte_energia = randint(-100, 300)
    if parte_tipo == "PECHO":
        parte_peso = randint(0, 35)
        parte_velocidad = randint(-20, 0)
        parte_slots_armas = 0
        parte_armadura = randint(-30, 50)
        parte_escudo = randint(-20, 50)
        parte_energia = randint(-100,400)
    if parte_tipo == "HOMBROS":
        parte_peso = randint(0, 10)
        parte_velocidad = randint(-5, 0)
        parte_slots_armas = 0
        parte_armadura = randint(-20, 30)
        parte_escudo = randint(-20, 50)
        parte_energia = randint(-100, 150)
    if parte_tipo == "PIERNAS":
        parte_peso = randint(0, 20)
        parte_velocidad = randint(-20, 50)
        parte_slots_armas = 0
        parte_armadura = randint(-30, 60)
        parte_escudo = randint(-20, 50)
        parte_energia = randint(-100,350)
    if parte_tipo == "BOTAS":
        parte_peso = randint(0, 10)
        parte_velocidad = randint(-10, 30)
        parte_slots_armas = 0
        parte_armadura = randint(-30, 25)
        parte_escudo = randint(-20, 20)
        parte_energia = randint(-100,200)
    if parte_tipo == "GUANTES":
        parte_peso = randint(0, 5)
        parte_velocidad = randint(-5, 5)
        parte_slots_armas = randint(0,1)
        parte_armadura = randint(-10, 10)
        parte_escudo = randint(-10, 10)
        parte_energia = randint(-100,150)
    if parte_tipo == "ALAS":
        parte_peso = randint(0, 10)
        parte_velocidad = randint(0, 70)
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
        esqueleto_velocidad = randint (0,200)
        esqueleto_slot_armas = randint (0, 3)
        esqueletos.append(Esqueleto(esqueleto_energia, esqueleto_movilidad, esqueleto_slot_armas, esqueleto_velocidad))
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
        jugador[2] = jugador[0].elegir_esqueleto(esqueletos)
        print(strftime("[%H:%M:%S]:"))
        print(strftime("[%H:%M:%S]:"),"TURNO DE:",jugador[0],"del",jugador[1],"!")
        sleep(0.3)
        print(strftime("[%H:%M:%S]:"),"ESQUELETO ELEGIDO:")
        sleep(0.1)
        print(strftime("[%H:%M:%S]:"),"Energia = ",jugador[2].get_energia())
        sleep(0.1)
        print(strftime("[%H:%M:%S]:"),"Velocidad =",jugador[2].get_velocidad())
        sleep(0.1)
        print(strftime("[%H:%M:%S]:"),"Movilidad =",jugador[2].get_movilidad())
        sleep(0.1)
        print(strftime("[%H:%M:%S]:"),"Max armas =",jugador[2].get_cantidad_slots())
        sleep(0.5)

def encolar_lista(lista):
    """Recibe una lista y la devuelve encolada"""
    nueva_cola = Cola()
    for item in lista:
        nueva_cola.encolar(item)
    return nueva_cola

def repartir_armas_partes(jugadores_encolados,partes_apiladas,armas_apiladas):
    """Recibe la cola de jugadores, la lista de partes y la de armas, luego hace que estos en su turno recojan aleatoriamente (la agreguen a la lista de personajes y sus caracteristicas) un arma o parte que este en el tope de su respectiva fila, los jugadores se vuelven a encolar hasta que ambas listas queden vacias. Cada jugador debe tener al meno un arma"""
    while not partes_apiladas.esta_vacia() or not armas_apiladas.esta_vacia():
        jugador = jugadores_encolados.desencolar()
        if partes_apiladas.esta_vacia() or len(jugador[4]) == 0:
            objeto_a_elegir = "ARMAS"
        elif armas_apiladas.esta_vacia():
            objeto_a_elegir = "PARTES"
        else:
            objeto_a_elegir = choice(["ARMAS", "PARTES"])
        if objeto_a_elegir == "PARTES":
            parte_elegida = partes_apiladas.desapilar()
            jugador[3][parte_elegida.get_tipo_parte()].append(parte_elegida)
        if objeto_a_elegir == "ARMAS":
            jugador[4].append(armas_apiladas.desapilar())
            print(strftime("[%H:%M:%S]: ")+str(jugador[0])+" del "+jugador[1]+" ha elegido un arma")
        jugadores_encolados.encolar(jugador)

def elegir_partes(jugadores_encolados):
    """Recibe la cola de jugadores y a cada uno lo hace quedarse con una parte de cada tipo, si es que cuentan con todos los tipos de armas, y las demas son desechadas"""
    cola_aux = Cola()
    while not jugadores_encolados.esta_vacia():
        jugador = jugadores_encolados.desencolar()
        cola_aux.encolar(jugador)
        jugador[3] = jugador[0].elegir_combinacion(jugador[3])
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
            if len(jugador[4]) == 0:
                break
            aux = choice(jugador[4])
            jugador[4].remove(aux)
            lista_aux.append(aux)
        jugador[4] = lista_aux
    while not cola_aux.esta_vacia():
        jugadores_encolados.encolar(cola_aux.desencolar())

def gunpla_por_velocidad(jugadores_encolados):
    '''Recibe la cola de jugadores, fabrica sus gumplas y devuelve una nueva cola con los jugadores encolados por velocidad (mayor a menor)'''
    nueva_cola = Cola()
    nueva_lista = []
    while not jugadores_encolados.esta_vacia():
        jugador = jugadores_encolados.desencolar()
        jugador[0].set_gunpla(Gunpla(jugador[2],jugador[3],jugador[4]))
        nueva_lista.append([jugador[0],jugador[1]])
    quick_sort_velocidad(nueva_lista)
    nueva_lista = list(reversed(nueva_lista))
    for piloto_gunpla in nueva_lista:
        nueva_cola.encolar(piloto_gunpla)
    return nueva_cola

def iniciar_batalla(gunplas_encolados, cant_equipos, cant_pilotos):
    cola_jugadores_enlistada = enlistar_cola(gunplas_encolados)
    equipos = []
    muertos = []
    for i in range(cant_equipos):
        equipos.append([])
    for jugador in cola_jugadores_enlistada:
        n_equipo = jugador[1].split(" ")[1]
        equipos[int(n_equipo)-1].append(jugador)
    jugadores_vivos_x_equipo = 2
    total_turnos = 0
    while jugadores_vivos_x_equipo > 1 and (total_turnos < (cant_pilotos*600)):
        total_turnos +=1
        jugador_atacante = gunplas_encolados.desencolar()
        if jugador_atacante in muertos:
            continue
        jugador_atacante[0].get_gunpla().actualizar_cooldowns()
        jugador_atacado = elegir_objetivo(jugador_atacante, equipos)
        arma_elegida = elegir_arma_de_turno(jugador_atacante)
        if arma_elegida == False:
            continue
        dano_lanzado = atacar(jugador_atacante, arma_elegida, False)
        dano_luego_de_defensas = aplicar_defensas(jugador_atacado, arma_elegida, dano_lanzado)
        analizar_turno(jugador_atacante, jugador_atacado, dano_luego_de_defensas, gunplas_encolados, equipos, arma_elegida, muertos)
        jugadores_vivos_x_equipo = 0
        for equipo_a_analizar in equipos:
            if len(equipo_a_analizar) != 0:
                jugadores_vivos_x_equipo += 1
        if jugador_atacante in muertos:
            continue
        gunplas_encolados.encolar(jugador_atacante)
    if (total_turnos == (cant_pilotos*600)):
        print(strftime("[%H:%M:%S]:"))
        print(strftime("[%H:%M:%S]: ")+"Cantidad de turnos maxima superada! No existe ganador, la pelea seguira hasta el fin de los tiempos!")
    else:
        k = 0
        for equipo in equipos:
            k+=1
            if len(equipo) != 0:
                print(strftime("[%H:%M:%S]:"))
                print(strftime("[%H:%M:%S]: ")+"EL EQUIPO",k,"ES EL GANADOR!")

def elegir_objetivo(atacante, equipos):
    '''recibe el atacante y la lista de equipos y elije y devuelve un objetivo de otro equipo'''
    enemigos = []
    for equipo in equipos:
        for jugador in equipo:
            if jugador != atacante and jugador[1] != atacante[1]:
                enemigos.append(jugador)
    return atacante[0].elegir_oponente(enemigos)

def elegir_arma_de_turno(jugador_atacante):
    contador = 0
    arma = jugador_atacante[0].elegir_arma(jugador_atacante[0].get_gunpla().get_armamento())
    if arma == False:
        return False
    while not jugador_atacante[0].get_gunpla().arma_disponible(arma):
        arma = jugador_atacante[0].elegir_arma(jugador_atacante[0].get_gunpla().get_armamento())
        contador += 1
        if contador == 8:
            return False
    if arma.get_tiempo_recarga() !=0:
        jugador_atacante[0].get_gunpla().iniciar_cooldown(arma)
    return arma

def atacar(atacante, arma_elegida, contraataque, dano_acumulado=0):
    for i in range(arma_elegida.get_hits()):
        probabilidad_multiplicador = randint(0, 100)
        if probabilidad_multiplicador == 0:
            dano_arma = 0
        if probabilidad_multiplicador <= (arma_elegida.get_presicion()*25):
            dano_arma = arma_elegida.get_dano()*1.5
        else:
            dano_arma = arma_elegida.get_dano()
        dano_acumulado += dano_arma

    if contraataque == False:
        probabilidad_de_combinar = randint(0,100)
        if arma_elegida.get_tipo() == "MELEE":
            if probabilidad_de_combinar <= 40:
                dano_acumulado += intentar_combinar(atacante, arma_elegida, dano_acumulado)
        if arma_elegida.get_tipo() == "RANGO":
            if probabilidad_de_combinar <= 25:
                dano_acumulado += intentar_combinar(atacante, arma_elegida, dano_acumulado)
    return dano_acumulado

def intentar_combinar(atacante, arma_elegida, dano_acumulado):
    for arma_a_analizar in atacante[0].get_gunpla().get_armamento():
        if (atacante[0].get_gunpla().arma_disponible(arma_a_analizar)) and (arma_elegida.get_tipo() == arma_a_analizar.get_tipo()) and (arma_elegida.get_clase() == arma_a_analizar.get_clase()):
            return atacar(atacante, arma_a_analizar, False, dano_acumulado)
        return 0

def aplicar_defensas(jugador_atacado, arma_elegida, dano_lanzado):
    probabilidad_de_evasion = uniform(0.00,100.00)
    if probabilidad_de_evasion <= (jugador_atacado[0].get_gunpla().get_movilidad()*80):
        return 0
    if arma_elegida.get_tipo_municion() == "FISICA":
        return (dano_lanzado - jugador_atacado[0].get_gunpla().get_armadura())
    if arma_elegida.get_tipo_municion() == "LASER":
        return dano_lanzado - (dano_lanzado * (jugador_atacado[0].get_gunpla().get_escudo()/100))
    if arma_elegida.get_tipo_municion() == "HADRON":
        return dano_lanzado

def analizar_turno(jugador_atacante, jugador_atacado, dano_luego_de_defensas, gunplas_encolados, equipos, arma_elegida, muertos):
    oponente_destruido = False
    if dano_luego_de_defensas == 0:
        gunplas_encolados.encolar(jugador_atacado)
    if dano_luego_de_defensas < 0:
        jugador_atacado[0].get_gunpla().absorb_energia(abs(dano_luego_de_defensas))
        gunplas_encolados.encolar(jugador_atacado)
    if dano_luego_de_defensas > 0:
        jugador_atacado[0].get_gunpla().lose_energia(dano_luego_de_defensas)
        if jugador_atacado[0].get_gunpla().get_energia_restante() < 0:
            if abs(jugador_atacado[0].get_gunpla().get_energia_restante()) > (jugador_atacado[0].get_gunpla().get_energia()/0.05):
                gunplas_encolados.encolar(jugador_atacante)
            print(strftime("[%H:%M:%S]: ")+"El",jugador_atacado[0],"del", jugador_atacado[1], "ha sido destruido!")
            equipos[int(jugador_atacado[1].split(" ")[1])-1].remove(jugador_atacado)
            muertos.append(jugador_atacado)
            oponente_destruido = True
    if (arma_elegida.get_tipo == "MELEE") and (not oponente_destruido):
        arma_contra = elegir_arma_de_turno(jugador_atacante)
        dano_contra = atacar(jugador_atacado, arma_contra, True)
        dano_luego_de_defensas_contra = aplicar_defensas(jugador_atacante, arma_contra, dano_contra)
        if dano_luego_de_defensas_contra < 0:
            jugador_atacante[0].get_gunpla().absorb_energia(abs(dano_luego_de_defensas_contra))
        if dano_luego_de_defensas_contra > 0:
            jugador_atacante[0].get_gunpla().lose_energia(dano_luego_de_defensas)
            if jugador_atacante[0].get_gunpla().get_energia_restante() < 0:
                equipos[int(jugador_atacado[1].split(" ")[1]) - 1].remove(jugador_atacado)






main()




