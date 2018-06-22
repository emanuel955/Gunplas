from random import randint, choice, uniform

class Arma:
    def __init__(self, peso, tipo, clase, municion, velocidad, armadura, escudo, energia, tiempo_recarga, dano, hits, presicion):
        self.peso = peso
        self.tipo = tipo
        self.clase = clase
        self.municion = municion
        self.velocidad = velocidad
        self.armadura = armadura
        self.escudo = escudo
        self.energia = energia
        self.dano = dano
        self.hits = hits
        self.presicion = presicion
        self.tiempo_recarga = tiempo_recarga
        self.esta_lista = True

    def __repr__(self):
        return "["+str(self.peso)+"kg, Tipo:"+self.tipo+", Clase:"+self.clase+", Municion:"+self.municion+", "+str(self.velocidad)+"Km/h, Armor:"+str(self.armadura)+", Escu:"+str(self.escudo)+", Energ:"+str(self.energia)+", Daño:"+str(self.dano)+", Hits:"+str(self.hits)+", "+str(self.presicion)+"%, Tiemp. Rec:"+str(self.tiempo_recarga)+"]"

    def get_peso(self):
        '''devuelve el peso'''
        return self.peso

    def get_tipo(self):
        '''devuelve el tipo'''
        return self.tipo

    def get_clase(self):
        '''devuelve la clase'''
        return self.clase

    def get_tipo_municion(self):
        '''devuelve el tipo de municion'''
        return self.municion

    def get_armadura(self):
        '''devuelve la armadura'''
        return self.armadura

    def get_escudo(self):
        '''devuelve el escudo'''
        return self.escudo

    def get_velocidad(self):
        '''devuelve la velocidad'''
        return self.velocidad

    def get_energia(self):
        '''devuelve la energia'''
        return self.energia

    def get_dano(self):
        '''devuelve el daño'''
        return self.dano

    def get_hits(self):
        '''devuelve los hits'''
        return self.hits

    def get_presicion(self):
        '''devuelve la presicion'''
        return self.presicion

    def esta_lista(self):
        '''devuelve si esta lista o no el arma'''
        return self.esta_lista

    def get_tipo_parte(self):
        '''devuelve siempre "arma"'''
        return "ARMA"

    def get_tiempo_recarga(self):
        '''devuelve el tiempo de recarga'''
        return self.tiempo_recarga

class Gunpla:
    def __init__(self, esqueleto, partes = None, armas = [Arma(1, "MELEE", "SPOON", "FISICA", 1, 0, 0, 0, 0, 1, 10, 0.10)]):
        self.esqueleto = esqueleto
        self.partes = partes
        self.armas = armas
        self.energia_restante = self.get_energia()
        self.cooldown = {}

    def __repr__(self):
        return "["+str(self.esqueleto)+" ,"+str(self.partes)+" ,"+str(self.armas)+"]"

    def arma_disponible(self,arma):
        '''recibe el arma y devuelve si esta o no disponible'''
        if arma in self.cooldown:
            return False
        else:
            return True

    def iniciar_cooldown(self, arma):
        '''recibe un arma e inicia su cooldown'''
        if not self.arma_disponible(arma):
            raise Exception ("Ya esta en cooldown")
        else:
            self.cooldown[arma] = arma.get_tiempo_recarga()

    def actualizar_cooldowns(self):
        '''actualiza los cooldowns de todas las armas'''
        aux = {}
        for arma in self.cooldown:
            if self.cooldown.get(arma) != 1:
                aux[arma] = (self.cooldown.get(arma) - 1)
        self.cooldown = aux

    def absorb_energia(self, energia):
        '''absorbe energia recibida y se la suma al gunpla'''
        self.energia_restante += energia

    def lose_energia(self, energia):
        '''pierde el valor de energia recibido'''
        self.energia_restante -= energia

    def get_peso(self):
        '''devuelve el peso total del gunpla'''
        contador = 0
        for parte in self.partes:
            if parte.get_armamento() != 0:
                lista_aux = parte.get_armamento()
                for arma in lista_aux:
                    contador += arma.get_peso()
            contador += parte.get_peso()
        for arma in self.armas:
            contador += arma.get_peso()
        return contador

    def get_armadura(self):
        '''devuelve la armadura total del gunpla'''
        contador = 0
        for parte in self.partes:
            if parte.get_armamento() != 0:
                lista_aux = parte.get_armamento()
                for arma in lista_aux:
                    contador += arma.get_armadura()
            contador += parte.get_armadura()
        for arma in self.armas:
            contador += arma.get_armadura()
        return contador

    def get_escudo(self):
        '''devuelve el escudo total del gunpla'''
        contador = 0
        for parte in self.partes:
            if parte.get_armamento() != 0:
                lista_aux = parte.get_armamento()
                for arma in lista_aux:
                    contador += arma.get_escudo()
            contador += parte.get_escudo()
        for arma in self.armas:
            contador += arma.get_escudo()
        return contador

    def get_velocidad(self):
        '''devuelve la velocidad total del gunpla'''
        contador = 0
        for parte in self.partes:
            if parte.get_armamento() != 0:
                lista_aux = parte.get_armamento()
                for arma in lista_aux:
                    contador += arma.get_velocidad()
            contador += parte.get_velocidad()
        for arma in self.armas:
            contador += arma.get_velocidad()
        contador += self.esqueleto.get_velocidad()
        return contador

    def get_energia(self):
        '''devuelve la energia inicial del gunpla'''
        contador = 0
        for parte in self.partes:
            if parte.get_armamento() != 0:
                lista_aux = parte.get_armamento()
                for arma in lista_aux:
                    contador += arma.get_energia()
            contador += parte.get_energia()
        for arma in self.armas:
            contador += arma.get_energia()
        contador += self.esqueleto.get_energia()
        return contador

    def get_energia_restante(self):
        '''devuelve la energia restante del gunpla'''
        return self.energia_restante

    def get_movilidad(self):
        '''devuelve la movilidad total del gunpla'''
        base = self.esqueleto.get_movilidad()
        movilidad = ((base - self.get_peso()) / (2 + self.get_velocidad() * 3)) / base
        if movilidad > 1:
            return 1
        if movilidad < 0:
            return 0
        return movilidad

    def get_armamento(self):
        '''devuelve las armas totales del gunpla'''
        total_armas = []
        for parte in self.partes:
            if parte.get_armamento() != 0:
                for arma_en_parte in parte.get_armamento():
                    total_armas.append(arma_en_parte)
        for arma_de_gunpla in self.armas:
            total_armas.append(arma_de_gunpla)
        if total_armas == None:
            return [Arma(1, "MELEE", "SPOON", "FISICA", 1, 0, 0, 0, 0, 1, 10, 0.10)]

        return total_armas

class Esqueleto:
    def __init__(self, energia, movilidad, max_armas, velocidad):
        self.energia = energia
        self.movilidad = movilidad
        self.max_armas = max_armas
        self.velocidad = velocidad


    def get_velocidad(self):
        return self.velocidad

    def get_energia(self):
        return self.energia

    def get_movilidad(self):
        return self.movilidad

    def get_cantidad_slots(self):
        return self.max_armas

    def __repr__(self):
        return "["+str(self.velocidad)+"Km/h, Movilidad:"+str(self.movilidad)+", Energ:"+str(self.energia)+", Max Armas:"+str(self.max_armas)+"]"

class Parte:
    def __init__(self, peso, armas_adosadas, velocidad, armadura, escudo, energia, tipo):
        self.peso = peso
        self.armas_adosadas = armas_adosadas
        self.velocidad = velocidad
        self.armadura = armadura
        self.escudo = escudo
        self.energia = energia
        self.tipo = tipo

    def __repr__(self):
        return "["+str(self.peso)+"kg, Tipo:"+self.tipo+", "+str(self.velocidad)+"Km/h, Armor:"+str(self.armadura)+", Escu:"+str(self.escudo)+", Energ:"+str(self.energia)+", Armamento:"+str(self.armas_adosadas)+"]"

    def get_peso(self):
        return self.peso

    def get_velocidad(self):
        return self.velocidad

    def get_armadura(self):
        return self.armadura

    def get_escudo(self):
        return self.escudo

    def get_energia(self):
        return self.energia

    def get_armamento(self):
        return self.armas_adosadas

    def get_tipo_parte(self):
        return self.tipo

class Piloto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.gunpla = None

    def __repr__(self):
        return self.nombre

    def set_gunpla(self,gunpla):
        self.gunpla = gunpla

    def get_gunpla(self):
        return self.gunpla

    def elegir_esqueleto(self, lista_esqueletos):
        esqueleto_elegido = choice(lista_esqueletos)
        return esqueleto_elegido

    def elegir_parte(self, partes_disponibles):
        tipos = list(partes_disponibles.keys())
        return choice(tipos)

    def elegir_combinacion(self, partes_reservadas):
        tipo_y_parte = {}
        while ("CASCO" not in tipo_y_parte) or ("PECHO" not in tipo_y_parte) or ("HOMBROS" not in tipo_y_parte) or ("PIERNAS" not in tipo_y_parte) or ("BOTAS" not in tipo_y_parte) or ("GUANTES" not in tipo_y_parte) or ("ALAS" not in tipo_y_parte) :
            tipo_elegido = self.elegir_parte(partes_reservadas)
            if (tipo_elegido not in tipo_y_parte) and (tipo_elegido in partes_reservadas) and (len(partes_reservadas[tipo_elegido]) != 0):
                tipo_y_parte[tipo_elegido] = choice(partes_reservadas[tipo_elegido])
                del partes_reservadas[tipo_elegido]
            elif (len(partes_reservadas[tipo_elegido]) == 0):
                del partes_reservadas[tipo_elegido]
            if not partes_reservadas:
                partes_reservadas = list(tipo_y_parte.values())
                break
        return partes_reservadas

    def elegir_oponente(self, oponentes):
        return choice(oponentes)

    def elegir_arma(self, oponente):
        escudo = oponente[0].get_gunpla().get_escudo()
        armadura = oponente[0].get_gunpla().get_armadura()
        if escudo > armadura:
            print(oponente[0],"especializado en defensas fisicas")
        if escudo > armadura:
            print(oponente[0],"especializado en defensas laser")
        else:
            print(oponente[0], "especializado en defensas laser y fisicas")
        armamento = self.get_gunpla().get_armamento()
        if len(armamento) == 0:
            return False
        return choice(armamento)

def elegir_esqueletos(jugadores, esqueletos):
    """Recibe la lista de jugadores y la de esqueletos y hace que estos los elijan aleatoriamente"""
    for jugador in jugadores:
        jugador[2] = jugador[0].elegir_esqueleto(esqueletos)

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
            print(str(jugador[0])+" DEL "+jugador[1]+" HA ELEGIDO UN ARMA")
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

def iniciar_batalla(gunplas_encolados, cant_equipos, cant_pilotos):
    '''Recibe la cola de Gunplas, la cantidad de equipos y pilotos, y lleva a cabo las funciones necesarias para que la batalla se ejecute'''
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
    while jugadores_vivos_x_equipo > 1 and (total_turnos < (cant_pilotos*1000)):
        total_turnos +=1
        jugador_atacante = gunplas_encolados.desencolar()
        if jugador_atacante in muertos:
            continue
        jugador_atacante[0].get_gunpla().actualizar_cooldowns()
        jugador_atacado = elegir_objetivo(jugador_atacante, equipos)
        arma_elegida = elegir_arma_de_turno(jugador_atacante, jugador_atacado)
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
        print()
        print("Cantidad de turnos maxima superada! No existe ganador, la pelea seguira hasta el fin de los tiempos!")
    else:
        k = 0
        for equipo in equipos:
            k+=1
            if len(equipo) != 0:
                print()
                print("EL EQUIPO",k,"ES EL GANADOR!")

def elegir_objetivo(atacante, equipos):
    '''recibe el atacante y la lista de equipos y elije y devuelve un objetivo de otro equipo'''
    enemigos = []
    for equipo in equipos:
        for jugador in equipo:
            if jugador != atacante and jugador[1] != atacante[1]:
                enemigos.append(jugador)
    return atacante[0].elegir_oponente(enemigos)

def elegir_arma_de_turno(jugador_atacante, jugador_atacado):
    '''Recibe al jugador atacante y al atacado y lo hace elegir un arma de su arsenal, si esta esta en cooldown elige otra, si no tiene ninguna disponible devuelve False'''
    contador = 0
    arma = jugador_atacante[0].elegir_arma(jugador_atacado)
    if arma == False:
        return False
    while not jugador_atacante[0].get_gunpla().arma_disponible(arma):
        arma = jugador_atacante[0].elegir_arma(jugador_atacado)
        contador += 1
        if contador == 8:
            return False
    if arma.get_tiempo_recarga() !=0:
        jugador_atacante[0].get_gunpla().iniciar_cooldown(arma)
    return arma

def atacar(atacante, arma_elegida, contraataque, dano_acumulado=0):
    '''Recibe al atacante, el arma, si es o no un contraataque (para ver si puede o no tratar de combinar) y, si fue llamada recursivamente, el daño acumulado, luego devuelve el daño total'''
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
    '''recibe el atacante, el arma y el daño acumulado e intenta combinar, si no lo logra, devuelve 0'''
    for arma_a_analizar in atacante[0].get_gunpla().get_armamento():
        if (atacante[0].get_gunpla().arma_disponible(arma_a_analizar)) and (arma_elegida.get_tipo() == arma_a_analizar.get_tipo()) and (arma_elegida.get_clase() == arma_a_analizar.get_clase()):
            return atacar(atacante, arma_a_analizar, False, dano_acumulado)
        return 0

def aplicar_defensas(jugador_atacado, arma_elegida, dano_lanzado):
    '''Recibe el jugador atacado, el arma y el daño e intenta, si es posible, defenderse, devuelve el daño recibido luego de aplicar sus defensas'''
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
    '''recibe el atacante, la victima, el daño, la cola de gunplas, la lista de equipos, el arma y la lista de muertos y analiza el turno, aplicando el daño realizado, fijandose si el oponente fue destruido, si hay posibilidad de contraatacar y si es necesario encolar turnos extra'''
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
            print("EL",jugador_atacado[0],"DEL", jugador_atacado[1], "HA SIDO DESTRUIDO")
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
