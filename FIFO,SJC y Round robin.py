import matplotlib.pyplot as plt
from queue import PriorityQueue

class Proceso:
    def __init__(self, id, tiempo_llegada, tiempo_ejecucion, prioridad):
        self.id = id
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad

    def __lt__(self, otro):
        # Se define el operador de comparación para la prioridad en la cola de prioridad
        return self.prioridad < otro.prioridad

def fifo(procesos):
    # Ordenar los procesos por tiempo de llegada
    procesos.sort(key=lambda x: x.tiempo_llegada)
    
    tiempo_actual = 0
    orden_ejecucion = []
    tiempos_espera = []

    for proceso in procesos:
        tiempo_espera = max(0, tiempo_actual - proceso.tiempo_llegada)
        tiempos_espera.append(tiempo_espera)
        tiempo_actual += proceso.tiempo_ejecucion
        orden_ejecucion.append(proceso.id)

    return orden_ejecucion, tiempos_espera

def sjf(procesos):
    cola_listos = PriorityQueue()
    tiempo_actual = 0
    orden_ejecucion = []
    tiempos_espera = []

    for proceso in procesos:
        cola_listos.put(proceso)

    while not cola_listos.empty():
        proceso_actual = cola_listos.get()
        tiempo_espera = max(0, tiempo_actual - proceso_actual.tiempo_llegada)
        tiempos_espera.append(tiempo_espera)
        tiempo_actual += proceso_actual.tiempo_ejecucion
        orden_ejecucion.append(proceso_actual.id)

    return orden_ejecucion, tiempos_espera

def round_robin(procesos, quantum):
    n = len(procesos)
    tiempo_actual = 0
    tiempo_ejecucion_restante = [proceso.tiempo_ejecucion for proceso in procesos]
    orden_ejecucion = []
    tiempos_espera = []

    while True:
        terminado = True
        for i in range(n):
            if tiempo_ejecucion_restante[i] > 0:
                terminado = False
                if tiempo_ejecucion_restante[i] > quantum:
                    tiempo_actual += quantum
                    tiempo_ejecucion_restante[i] -= quantum
                else:
                    tiempo_actual += tiempo_ejecucion_restante[i]
                    tiempo_espera.append(max(0, tiempo_actual - procesos[i].tiempo_llegada - procesos[i].tiempo_ejecucion))
                    orden_ejecucion.append(procesos[i].id)
                    tiempo_ejecucion_restante[i] = 0

        if terminado:
            break

    return orden_ejecucion, tiempos_espera

def graficar(algoritmo, procesos, quantum=None):
    if algoritmo == "FIFO":
        orden_ejecucion, tiempos_espera = fifo(procesos)
    elif algoritmo == "SJF":
        orden_ejecucion, tiempos_espera = sjf(procesos)
    elif algoritmo == "Round Robin":
        orden_ejecucion, tiempos_espera = round_robin(procesos, quantum)
    else:
        print("Algoritmo no válido")
        return

    # Graficar
    plt.figure(figsize=(10, 6))
    for i in range(len(orden_ejecucion)):
        plt.plot([i, i+1], [orden_ejecucion[i], orden_ejecucion[i]], color='blue', linewidth=2)
    plt.xlabel('Tiempo')
    plt.ylabel('Proceso')
    plt.title(f'Progreso de cada Proceso usando {algoritmo}')
    plt.grid(True)
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    procesos = [
        Proceso(1, 0, 6, 3),
        Proceso(2, 1, 4, 1),
        Proceso(3, 2, 2, 2),
        Proceso(4, 3, 1, 3)
    ]

    algoritmo = input("Elija el algoritmo a utilizar (FIFO, SJF, Round Robin): ")
    if algoritmo == "Round Robin":
        quantum = int(input("Ingrese el tamaño del quantum para Round Robin: "))
        graficar(algoritmo, procesos, quantum)
    else:
        graficar(algoritmo, procesos)
