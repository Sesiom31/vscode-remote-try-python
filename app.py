#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write "hello world" to the console
print("hello world")

# minijuego piedra papel y tijera
# importar la libreria random
import random

# definir las opciones
opciones = ["piedra", "papel", "tijera"]
seguirJugando = 'si'

# definir la funcion que va a jugar

def jugar():
    global seguirJugando
    triunfos = 0
    rondas = 0
    while(seguirJugando == 'si'):
        # pedir al usuario que elija una opcion
        opcionUsuario = input("Elige una opcion: piedra, papel o tijera: ")
        # elegir una opcion al azar

        if opcionUsuario not in opciones:
            print("Opcion invalida!")
            continue

        opcionComputadora = random.choice(opciones)
        rondas += 1
        # mostrar la opcion de la computadora
        print("La computadora eligio: " + opcionComputadora)
        # determinar el ganador
        if opcionUsuario == opcionComputadora:
            print("Empate!")
        elif opcionUsuario == "piedra":
            if opcionComputadora == "papel":
                print("Perdiste!")
            else:
                triunfos += 1
                print("Ganaste!")
        elif opcionUsuario == "papel":
            if opcionComputadora == "tijera":
                print("Perdiste!")
            else:
                triunfos += 1
                print("Ganaste!")
        elif opcionUsuario == "tijera":
            if opcionComputadora == "piedra":
                print("Perdiste!")
            else:
                triunfos += 1
                print("Ganaste!")
        # preguntar si quiere seguir jugando
        seguirJugando = input("Quieres seguir jugando? si/no: ")
        # si no quiere seguir jugando, terminar el juego

        while(seguirJugando != 'si' and seguirJugando != 'no'):
            print("Opcion invalida!")
            seguirJugando = input("Quieres seguir jugando? si/no: ")

        if seguirJugando == 'no':
            print("Has ganado " + str(triunfos) + " de " + str(rondas) + " rondas")
            print("Gracias por jugar!")
            break

# jugar
jugar()
