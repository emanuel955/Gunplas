from random import randint

def main():
    cant_pilotos = 1
    while es_primo(cant_pilotos):    #La cantidad de pilotos debe ser si o si un numero no primo para poder dividirlos en grupos iguales
        cant_pilotos = randint(2,20)
    print (cant_pilotos) #Prueba
    cant_equipos = randint(2, 5)
    while (cant_pilotos % cant_equipos != 0) or (cant_pilotos / cant_equipos > 5):   #Para que todos los equipos tengan la misma cantidad de jugadores y esta no sea mayor a 5
        cant_equipos = randint(2,5)
    print (cant_equipos) #Prueba


def es_primo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
