import serial
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Configura el puerto serie. Asegúrate de que el nombre del puerto es el correcto.
ser = serial.Serial('COM6', 9600, timeout=1) 

# Define el umbral del sensor
umbral_sensor = 500

# Nombre del archivo CSV
nombre_archivo = 'datos_umbral_prueba_con_1mili.csv'

# Listas para almacenar los datos para el gráfico
tiempos = []
valores_sensor = []

# Abre el archivo CSV en modo escritura
with open(nombre_archivo, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribe la cabecera del archivo CSV
    writer.writerow(['Tiempo', 'Valor del sensor', 'Estado del LED'])
    
    try:
        while True:
            # Lee una línea del puerto serie
            line = ser.readline().decode('utf-8').strip()
            if line:
                # Divide la línea en dos variables
                variables = line.split(',')
                if len(variables) == 2:
                    # Convierte las variables a los tipos adecuados
                    sensorValue = int(variables[0])
                    ledState = int(variables[1])
                    tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtener el tiempo actual

                    # Escribe las variables en el archivo CSV
                    writer.writerow([tiempo, sensorValue, ledState])
                    print(f"Datos guardados: {variables}")

                    # Guardar los datos para el gráfico
                    tiempos.append(tiempo)
                    valores_sensor.append(sensorValue)

                    # Comprobar si el valor del sensor está por debajo del umbral
                    if sensorValue < umbral_sensor:
                        print("Sensor comenzó a medir")

                    # Graficar los datos
                    plt.clf()  # Limpiar el gráfico
                    plt.plot(tiempos, valores_sensor, label="Valor del sensor")
                    plt.axhline(y=umbral_sensor, color='r', linestyle='--', label="Umbral del sensor")
                    plt.xlabel('Tiempo')
                    plt.ylabel('Valor del sensor')
                    plt.title('Lecturas del sensor en el tiempo')
                    plt.legend()
                    plt.gcf().autofmt_xdate()  # Formatear las etiquetas de tiempo
                    plt.pause(0.001)  # Pausar para actualizar el gráfico

    except KeyboardInterrupt:
        print("Interrupción por teclado. Cerrando archivo.")
        ser.close()
        plt.show()  # Mostrar el gráfico final
