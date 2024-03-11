import matplotlib.pyplot as plt

def round_robin(procesos, quantum):
    n = len(procesos)
    tiempo_actual = 0
    tiempo_ejecucion_restante = [proceso[1] for proceso in procesos]  # Tiempo de ráfaga restante para cada proceso
    tiempo_finalizacion = [0] * n  # Tiempo de finalización de cada proceso
    tiempo_espera = [0] * n  # Tiempo de espera para cada proceso

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
                    tiempo_espera[i] = tiempo_actual - procesos[i][1]
                    tiempo_ejecucion_restante[i] = 0
                    tiempo_finalizacion[i] = tiempo_actual

        if terminado:
            break

    # Imprimir los resultados
    print("Proceso\t\tTiempo de Ráfaga\t\tTiempo de Finalización\t\tTiempo de Espera")
    for i in range(n):
        print(f"{procesos[i][0]}\t\t{procesos[i][1]}\t\t\t{tiempo_finalizacion[i]}\t\t\t{tiempo_espera[i]}")

    # Crear una gráfica para visualizar el progreso de cada proceso desde el tiempo de llegada hasta el tiempo de finalización
    plt.figure(figsize=(10, 6))
    for i in range(n):
        plt.plot([procesos[i][1], tiempo_finalizacion[i]], [procesos[i][0]] * 2, color='blue', linewidth=2)
    plt.xlabel('Tiempo')
    plt.ylabel('Proceso')
    plt.title('Progreso de cada Proceso desde Tiempo de Llegada hasta Tiempo de Finalización (Round Robin)')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Datos predefinidos: (nombre, tiempo de ráfaga)
    procesos = [("P1", 10), ("P2", 5), ("P3", 8), ("P4", 4)]
    quantum = 2  # Tamaño del quantum

    # Ejecutar el algoritmo Round Robin con los datos predefinidos
    print("Algoritmo Round Robin\n")
    round_robin(procesos, quantum)
