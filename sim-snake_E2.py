import random
# Obtener cantidad de jugadores
num_jugadores = int(input("Ingrese la cantidad de jugadores: "))

# Diccionario para almacenar la información de cada jugador
jugadores = {}
nombres = ['Juan', 'María', 'Pedro', 'Ana']
for i in range(num_jugadores):
   
    nombre = nombres[i]
    jugadores[nombre] = {
        'posicion': 0,
        'turnos': 0
    }

import time

# Variable para almacenar el tiempo de inicio
#tiempo_inicio = time.time()

# tablero con serpientes y escaleras
serpientes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

escaleras = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

def tirar_dado():
    resultado = random.randint(1, 6)
    #extra dice
    if resultado == 6:
        print("¡Sacaste un 6! Tirás de nuevo")
        return resultado + tirar_dado()
    return resultado


def jugar():
    # Lista para almacenar las posiciones de todos los jugadores
    jugadores = []
    for i in range(num_jugadores):
        jugadores.append({
            'posicion': 0,
            'turnos': 0
        })
    
    jugador_actual = 0
    
    # Verificar si algún jugador llegó a 100
    hay_ganador = False
    while not hay_ganador:
        jugadores[jugador_actual]['turnos'] += 1
        dado = tirar_dado()
        posicion_anterior = jugadores[jugador_actual]['posicion']
        jugadores[jugador_actual]['posicion'] += dado
        
        print(f"Jugador {jugador_actual + 1} - Turno {jugadores[jugador_actual]['turnos']}: ")
        print(f"Dado = {dado}, Avanza de {posicion_anterior} a {jugadores[jugador_actual]['posicion']}")
        
        # Verificar si cayó en una serpiente
        if jugadores[jugador_actual]['posicion'] in serpientes:
            print(f"jajaja te agarró una serpiente en {jugadores[jugador_actual]['posicion']}. Caes hasta el casillero {serpientes[jugadores[jugador_actual]['posicion']]}")
            jugadores[jugador_actual]['posicion'] = serpientes[jugadores[jugador_actual]['posicion']]
        
        # Verificar si cayó en una escalera
        elif jugadores[jugador_actual]['posicion'] in escaleras:
            print(f"¡Biennn! Agarraste una escalera en {jugadores[jugador_actual]['posicion']}. Subiste hasta el casillero {escaleras[jugadores[jugador_actual]['posicion']]}")
            jugadores[jugador_actual]['posicion'] = escaleras[jugadores[jugador_actual]['posicion']]
            
        # Si se pasa de 100, vuelve a la posición anterior
        if jugadores[jugador_actual]['posicion'] > 100:
            print("Te pasaste del 100, volvés a tu posición anterior")
            jugadores[jugador_actual]['posicion'] = posicion_anterior
        
        # Verificar si cayó en casillero ocupado
        for otro_jugador in range(num_jugadores):
            if otro_jugador != jugador_actual and jugadores[jugador_actual]['posicion'] == jugadores[otro_jugador]['posicion']:
                print(f"¡Casillero ocupado! El jugador {otro_jugador + 1} retrocede 5 casilleros")
                jugadores[otro_jugador]['posicion'] = max(0, jugadores[otro_jugador]['posicion'] - 5)
            
        print(f"Posición final del turno: {jugadores[jugador_actual]['posicion']}\n")
        
        # Verificar si hay ganador
        if jugadores[jugador_actual]['posicion'] >= 100:
            hay_ganador = True
            ganador = jugador_actual
        else:
            # Cambiar al siguiente jugador
            jugador_actual = (jugador_actual + 1) % num_jugadores
    
    print(f"¡Felicitaciones Jugador {ganador + 1}! Llegaste a la meta en {jugadores[ganador]['turnos']} turnos")


# Ejecutar el juego
print("¡Bienvenido a Serpientes y Escaleras!")
jugar()
