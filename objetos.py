class Gunpla:
    def __init__(self, partes, armas):
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
    def __init__(self, peso, armas_adosadas, velocidad, armadura, escudo, energia):
        self.peso = peso
        self.armas_adosadas = armas_adosadas
        self.velocidad = velocidad
        self.armadura = armadura
        self.escudo = escudo
        self.energia = energia


    def get_peso(self):
        pass

    def get_armadura(self):
        pass

    def get_escudo(self):
        pass

    def get_velocidad(self):
        pass

    def get_energia(self):
        pass

    def get_armamento(self):
        pass

    def get_tipo_parte(self):
        pass


class Arma:
    def __init__(self, peso, tipo, clase, municion, velocidad, armadura, escudo, energia, tiempo_recarga, daño, hits, presicion):
        self.peso = peso
        self.tipo = tipo
        self.clase = clase
        self.municion = municion
        self.velocidad = velocidad
        self.armadura = armadura
        self.escudo = escudo
        self.energia = energia
        self.daño = daño
        self.hits = hits
        self.presicion = presicion
        self.tiempo_recarga = tiempo_recarga


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

