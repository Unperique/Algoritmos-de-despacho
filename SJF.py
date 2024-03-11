import matplotlib.pyplot as plt

def sjf(procesos, tiempos_llegada):
    # Ordenar los procesos por tiempo de ráfaga
    procesos.sort(key=lambda x: x[1])
    
    # Obtener la cantidad de procesos
    n = len(procesos)
    
    # Inicializar listas para almacenar los tiempos de finalización de cada proceso
    tiempo_finalizacion = [0] * n

    # Calcular los tiempos de finalización de cada proceso
    tiempo_finalizacion[0] = procesos[0][1] + procesos[0][2]  # Tiempo de finalización del primer proceso es el tiempo de llegada más su ráfaga
    for i in range(1, n):
        # Si el tiempo de llegada del proceso actual es mayor que el tiempo de finalización del proceso anterior,
        # el proceso actual comienza justo después de que finaliza el proceso anterior.
        tiempo_finalizacion[i] = max(procesos[i][2], tiempo_finalizacion[i-1]) + procesos[i][1]

    # Calcular los tiempos de espera para cada proceso
    tiempo_espera = [tiempo_finalizacion[i] - procesos[i][1] - procesos[i][2] for i in range(n)]

    # Calcular el tiempo total de espera del sistema y el promedio de espera del sistema
    tiempo_espera_total = sum(tiempo_espera)
    tiempo_espera_promedio = tiempo_espera_total / n

    # Calcular el tiempo total del sistema y el promedio del sistema
    tiempo_total_sistema = sum(tiempo_finalizacion) - sum(tiempos_llegada)
    tiempo_promedio_sistema = tiempo_total_sistema / n

    # Imprimir los resultados
    print("Proceso\t\tRáfaga\t\tTiempo_Llegada\t\tTiempo_Espera")
    for i in range(n):
        print(f"{procesos[i][0]}\t\t{procesos[i][1]}\t\t\t{procesos[i][2]}\t\t\t{tiempo_espera[i]}")
    print(f"\nTiempo total de espera del sistema: {tiempo_espera_total}")
    print(f"Tiempo promedio de espera del sistema: {tiempo_espera_promedio}")
    print(f"Tiempo total del sistema: {tiempo_total_sistema}")
    print(f"Tiempo promedio del sistema: {tiempo_promedio_sistema}")

    # Crear una gráfica para visualizar el progreso de cada proceso desde el tiempo de llegada hasta el tiempo de finalización
    plt.figure(figsize=(10, 6))
    for i in range(n):
        if i > 0:
            plt.plot([tiempo_finalizacion[i-1], tiempo_finalizacion[i]], [procesos[i][0]] * 2, color='blue', linewidth=2)
        else:
            plt.plot([procesos[i][2], tiempo_finalizacion[i]], [procesos[i][0]] * 2, color='blue', linewidth=2)
    plt.xlabel('Tiempo')
    plt.ylabel('Proceso')
    plt.title('Progreso de cada Proceso desde Tiempo de Llegada hasta Tiempo de Finalización (SJF)')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Datos predefinidos: (nombre, tiempo de ráfaga, tiempo de llegada)
    procesos = [("P1", 10, 0), ("P2", 5, 1), ("P3", 8, 2), ("P4", 4, 3)]

    # Ejecutar el algoritmo SJF con los datos predefinidos
    print("Algoritmo SJF\n")
    sjf(procesos, [proceso[2] for proceso in procesos])
