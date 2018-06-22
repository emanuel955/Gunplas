from random import choice

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

    def elegir_arma(self, armamento):
        if len(armamento) == 0:
            return False
        return choice(armamento)

class Nodo:
    def __init__(self, dato = None, prox = None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)

class ListaEnlazada:
    def __init__(self, prim = None):
        self.prim = prim
        self.len = 0

    def insert(self, x, i=0):
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, levanta IndexError"""
        if i < 0 or i > self.len:
            raise IndexError("Posición inválida")
        nuevo = Nodo(x)
        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len += 1

    def esta_vacia(self):
        if self.len == 0:
            return True
        else:
            return False

    def pop(self, i=None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento."""
        if i is None and self.esta_vacia():
            raise IndexError("Esta vacia")
        elif i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.len -= 1
        return dato

class Pila:
   def __init__(self):
      self.lista = ListaEnlazada()

   def __str__(self):
       return str(self.lista.len) + " elementos"

   def apilar(self, dato):
      self.lista.insert(dato)

   def desapilar(self):
      return self.lista.pop(0)

   def esta_vacia(self):
       if self.lista.len == 0:
           return True
       else:
           return False

class Cola:
    def __init__(self):
        self.lista = ListaEnlazada()

    def __str__(self):
        return str(self.lista.len) + " elementos"
        # return str(self.lista.prim.dato)

    def encolar(self,dato):
            self.lista.insert(dato)

    def desencolar(self):
        return self.lista.pop()

    def esta_vacia(self):
        if self.lista.len == 0:
            return True
        else:
            return False


