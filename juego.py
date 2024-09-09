#importamos la libreria para generar un número aleatorio
import random
#declaramos una variable para guardar el numero secreto
adivinar = ""
#usamos un ciclo para generar el numero secreto con digitos del 0 al 9
for i in range(4):
    posible= random.randint(0,9)
    while str(posible) in adivinar:
        posible= random.randint(0,9)
    adivinar+=str(posible)
#declaramos una variable para guardar el numero ingresado por el usuario
adivinado =input("Adivina el numero secreto: ")
#variable para guardar el numero de intentos
intentos = 1
#usamos un ciclo para contar la cantidad de coincidencias 
while adivinado != adivinar:
    intentos+=1
    fama = 0
    toque = 0
    #usamos un ciclo para evaluar cada posicion del numero ingresado 
    # y ver si se encuentra en el numero secreto con la funcion in
    for i in range(4):
        if adivinar[i] == adivinado[i]:
            fama+=1
        elif adivinar[i] in adivinado:
            toque+=1
    #muestra en pantalla la cantidad de famas y toques
    print(f"tu número tiene {fama} fama y {toque} toque")
    #pide al usuario ingresar un numero
    adivinado = input("Escribe otro número: ")
#muestra en pantalla el numero correcto al acertar
print (f"Felicitaciones! Adivinaste el número secreto en {intentos} intentos.")