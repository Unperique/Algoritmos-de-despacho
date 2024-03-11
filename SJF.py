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

def sjcf(procesos):
    cola_listos = PriorityQueue()
    tiempo_actual = 0
    orden_ejecucion = []
    tiempo_espera_total = 0
    tiempo_sistema_total = 0

    while not cola_listos.empty() or procesos:
        while procesos and procesos[0].tiempo_llegada <= tiempo_actual:
            proceso = procesos.pop(0)
            cola_listos.put(proceso)

        if cola_listos.empty():
            tiempo_actual = procesos[0].tiempo_llegada
            continue

        proceso_actual = cola_listos.get()

        # Tiempo de espera para este proceso
        tiempo_espera = tiempo_actual - proceso_actual.tiempo_llegada
        tiempo_espera_total += tiempo_espera

        quantum = min(2, proceso_actual.tiempo_ejecucion)
        for _ in range(quantum):
            orden_ejecucion.append(proceso_actual.id)
            tiempo_actual += 1
            proceso_actual.tiempo_ejecucion -= 1

            if proceso_actual.tiempo_ejecucion == 0:
                break

        if proceso_actual.tiempo_ejecucion > 0:
            cola_listos.put(proceso_actual)

        # Tiempo de sistema para este proceso
        tiempo_sistema = tiempo_espera + proceso_actual.tiempo_ejecucion
        tiempo_sistema_total += tiempo_sistema

    num_procesos = len(orden_ejecucion)
    promedio_tiempo_espera = tiempo_espera_total / num_procesos
    promedio_tiempo_sistema = tiempo_sistema_total / num_procesos

    return orden_ejecucion, promedio_tiempo_espera, promedio_tiempo_sistema

# Ejemplo de uso
if __name__ == "__main__":
    procesos = [
        Proceso(1, 0, 6, 3),
        Proceso(2, 1, 4, 1),
        Proceso(3, 2, 2, 2),
        Proceso(4, 3, 1, 3)
    ]

    orden_ejecucion, promedio_tiempo_espera, promedio_tiempo_sistema = sjcf(procesos)
    print("Orden de ejecución de los procesos:", orden_ejecucion)
    print("Promedio del tiempo de espera:", promedio_tiempo_espera)
    print("Promedio del tiempo de sistema:", promedio_tiempo_sistema)
