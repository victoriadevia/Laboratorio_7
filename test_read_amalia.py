import serial
import time
import csv

# Compu Bruno
# arduino = serial.Serial(port="/dev/ttyACM0",  baudrate=9600, timeout=.1)
# Compu Amalia
arduino = serial.Serial(port="COM6", baudrate=9600, timeout=.1)


def write_read():
    time.sleep(0.000001)
    data = arduino.readline()
    return data


eventos = []
start = time.time()
elapsed = 0
print("midiendo")
while elapsed < 5:
    value = write_read()
    value = value.decode('utf-8').strip()
    if value:  # Only add non-empty values
        # Convert the string to a tuple
        try:
            event = eval(value)
            if isinstance(event, tuple):
                eventos.append(event)
        except:
            print(f"Error processing value: {value}")
    end = time.time()
    elapsed = end - start

# Write events to a CSV file
csv_file = 'eventos_1millo_1millo_5seg.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    for event in eventos:
        writer.writerow(event)

print(f"Eventos guardados en {csv_file}")
