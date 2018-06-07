from random import randint

def main():
    cant_pilotos = 1
    while es_primo(cant_pilotos):    #La cantidad de pilotos debe ser si o si un numero no primo para poder dividirlos en grupos iguales
        cant_pilotos = randint(2,20)
    print ("Cantidad de pilotos: ", cant_pilotos) #Prueba
    cant_equipos = randint(2, 5)
    while (cant_pilotos % cant_equipos != 0) or (cant_pilotos / cant_equipos > 5):   #Para que todos los equipos tengan la misma cantidad de jugadores y esta no sea mayor a 5
        cant_equipos = randint(2,5)
    print ("Cantidad de equipos: ", cant_equipos) #Prueba
    equipos = []
    for equipo in range(cant_equipos):    #Creo un listado con los equipos, dentro de cada equipo por ahora dejo la cantidad de integrantes que tiene solo para hacer pruebas
        equipos.append([int(cant_pilotos / cant_equipos)])
    print("Listado de equipos: ", equipos) #Prueba



def es_primo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

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

