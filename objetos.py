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

<<<<<<< HEAD
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
    def __init__(self, peso, clase, tipo, municion, velocidad, armadura, escudo, energia, tiempo_recarga):
        self.peso = peso
        self.clase = clase
        self.tipo = tipo
        self.municion = municion
        self.velocidad = velocidad
        self.armadura = armadura
        self.escudo = escudo
        self.energia = energia
        self.tiempo_recarga = tiempo_recarga

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
=======
    def get_cantidaf_slots(self):
        pass


class Esqueleto:
    def __init__(self, armas_adosadas, velocidad, armadura, escudo, energia):
        self.
>>>>>>> 3668ba7e6807d0ccf315ef624b8d720f0fb19c72
