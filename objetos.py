class Gunpla:
    def __init__(self, esqueleto, partes = None, armas = None):
        self.esqueleto = esqueleto
        self.partes = partes
        self.armas = armas


    def get_peso(self):
        pass

    def get_armadura(self):
        pass

    def get_velocidad(self):
        pass

    def get_energia(self):
        pass

    def get_energia_restante(self):
        pass

    def get_movilidad(self):
        pass

    def get_armamento(self):
        pass


class Esqueleto:
    def __init__(self, energia, movilidad, max_armas):
        self.energia = energia
        self.movilidad = movilidad
        self.max_armas = max_armas


    def get_velocidad(self):
        pass

    def get_energia(self):
        pass

    def get_movilidad(self):
        pass

    def get_cantidad_slots(self):
        pass


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

    def __repr__(self):
        return "["+str(self.peso)+"kg, Tipo:"+self.tipo+", Clase:"+self.clase+", Municion:"+self.municion+", "+str(self.velocidad)+"Km/h, Armor:"+str(self.armadura)+", Escu:"+str(self.escudo)+", Energ:"+str(self.energia)+", Daño:"+str(self.dano)+", Hits:"+str(self.hits)+", "+str(self.presicion)+"%, Tiemp. Rec:"+str(self.tiempo_recarga)+"]"


    def get_peso(self):
        return self.peso

    def get_tipo(self):
        return self.tipo

    def get_clase(self):
        return self.clase

    def get_tipo_municion(self):
        return self.municion

    def get_armadura(self):
        return self.armadura

    def get_escudo(self):
        return self.escudo

    def get_velocidad(self):
        return self.velocidad

    def get_energia(self):
        return self.energia

    def get_daño(self):
        return self.daño

    def get_hits(self):
        return self.hits

    def get_presicion(self):
        return self.presicion

    def esta_lista(self):
        pass #AUN NO PUDEMOS HACER ESTA FUNCION

    def get_tipo_parte(self):
        return "ARMA"

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

    def pop(self, i=None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento."""
        if i is None:
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

class Pila(ListaEnlazada):

    def apilar(self, dato):
        self.insert(dato)

    def desapilar(self):
        self.pop(0)

def main():
    queso = Pila()
    queso.apilar(3)
    queso.apilar(4)
    queso.apilar(43)
    queso.apilar(46)
    pan = queso.desapilar()
    print(pan)


main()



