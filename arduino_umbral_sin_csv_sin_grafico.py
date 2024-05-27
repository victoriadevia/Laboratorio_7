import serial
from datetime import datetime, timedelta

# Configura el puerto serie. Asegúrate de que el nombre del puerto es el correcto.
ser = serial.Serial('COM6', 9600, timeout=1)

# Define el umbral del sensor
umbral_sensor = 500

# Variables para la lógica del umbral
umbral_alcanzado = False

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

                # Comprobar si el valor del sensor cruza el umbral en cualquier dirección
                if sensorValue < umbral_sensor and not umbral_alcanzado:
                    print("Sensor comenzó a medir")
                    umbral_alcanzado = True
                elif sensorValue >= umbral_sensor and umbral_alcanzado:
                    umbral_alcanzado = False

except KeyboardInterrupt:
    print("Interrupción por teclado. Cerrando el puerto serie.")
    ser.close()


