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
    turnos_totales = 0
    
    # Verificar si algún jugador llegó a 100
    hay_ganador = False
    while not hay_ganador:
        jugadores[jugador_actual]['turnos'] += 1
        turnos_totales += 1
        dado = tirar_dado()
        posicion_anterior = jugadores[jugador_actual]['posicion']
        jugadores[jugador_actual]['posicion'] += dado
        
        # Verificar si cayó en una serpiente
        if jugadores[jugador_actual]['posicion'] in serpientes:
            jugadores[jugador_actual]['posicion'] = serpientes[jugadores[jugador_actual]['posicion']]
        
        # Verificar si cayó en una escalera
        elif jugadores[jugador_actual]['posicion'] in escaleras:
            jugadores[jugador_actual]['posicion'] = escaleras[jugadores[jugador_actual]['posicion']]
            
        # Si se pasa de 100, vuelve a la posición anterior
        if jugadores[jugador_actual]['posicion'] > 100:
            jugadores[jugador_actual]['posicion'] = posicion_anterior
        
        # Verificar si hay ganador
        if jugadores[jugador_actual]['posicion'] >= 100:
            hay_ganador = True
            ganador = jugador_actual
        else:
            # Cambiar al siguiente jugador
            jugador_actual = (jugador_actual + 1) % num_jugadores
    
    return turnos_totales

# Ejecutar 70 simulaciones
print("Simulando 70 partidas...")
import pandas as pd

resultados = []
for i in range(10):
    turnos = jugar()
    resultados.append({'Partida': i+1, 'Turnos': turnos})
    print(f"Partida {i+1}: {turnos} turnos")

# Crear DataFrame y exportar a Excel
df = pd.DataFrame(resultados)
df.to_excel('c:\\Agus\\2025 1er cuatri\\Io2\\E1_resultados_simulacion_3players.xlsx', index=False)
print("\nResultados guardados en 'E1_resultados_simulacion_3players.xlsx'")

# Ejecutar el juego
print("¡Bienvenido a Serpientes y Escaleras!")
jugar()
