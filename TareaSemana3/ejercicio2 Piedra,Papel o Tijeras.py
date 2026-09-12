# Piedra, Papel o Tijeras

import random

posibles_jugadas = ["piedra", "papel", "tijeras", "tijera"]
jugadas = [jugada.capitalize() for jugada in posibles_jugadas]
jugadas_ia = ["Piedra", "Papel", "Tijeras"]

print("Juego de Piedra, Papel o Tijeras\n")
print("Elegiremos entre Piedra, Papel o Tijeras\n")
print("Piedra le gana a Tijeras / Tijeras le gana a Papel / Papel le gana a Piedra")

juega_ia = random.choice(jugadas_ia)

while True:

    jugada_player = input("==> ").capitalize()

    if jugada_player in jugadas:

        #Piedra-IA
        if juega_ia == jugadas_ia[0]:
            #Piedra-Player
            if jugada_player == jugadas[0]:
                print("Piedra! ..... Fue un empate. Intentemos denuevo\n")
                juega_ia = random.choice(jugadas_ia)
                continue
            #Papel-Player
            elif jugada_player == jugadas[1]:
                print("Piedra! ..... Ganaste!!\n")
                break
            #Tijeras-Player
            elif jugada_player == jugadas[2] or jugadas[3]:
                print("Piedra! ..... Perdiste. Intentalo denuevo\n")
                juega_ia = random.choice(jugadas_ia)
                continue

        #Papel-IA
        elif juega_ia == jugadas_ia[1]:
            #Piedra-Player
            if jugada_player == jugadas[0]:
                print("Papel! ..... Perdiste. Intentalo denuevo\n")
                juega_ia = random.choice(jugadas_ia)
                continue
            #Papel-Player
            elif jugada_player == jugadas[1]:
                print("Papel! ..... Fue un empate. Intentemos denuevo\n")
                juega_ia = random.choice(jugadas_ia)
                continue
            #Tijeras-Player
            elif jugada_player == jugadas[2] or jugadas[3]:
                print("Papel! ..... Ganaste!!")
                break

        #Tijera-IA
        elif juega_ia == jugadas_ia[2]:
            #Piedra-Player
            if jugada_player == jugadas[0]:
                print("Tijera! ..... Ganaste!!")
                break
            #Papel-Player
            elif jugada_player == jugadas[1]:
                print("Tijera! ..... Perdiste. Intentalo denuevo\n")
                juega_ia = random.choice(jugadas_ia)
                continue
            #Tijera-Player
            elif jugada_player == jugadas[2] or jugadas[3]:
                print("Tijera! ..... Fue un empate. Intentemos denuevo\n")
                juega_ia = random.choice(jugadas_ia)
                continue

    else:
        print("Elige una opcion valida ==> Piedra | Papel | Tijera")

