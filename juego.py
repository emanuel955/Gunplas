from random import randint

def main():
    pilotos = 1
    while es_primo(pilotos):    #la cantidad de pilotos debe ser si o si un numero no primo para poder dividirlos en grupos iguales
        pilotos = randint(1,20)
    print (pilotos)


def es_primo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

main()