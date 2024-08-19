import serial
import time

# Compu Bruno
#arduino = serial.Serial(port="/dev/ttyACM0",  baudrate=9600, timeout=.1)
# Compu Amalia
arduino = serial.Serial(port="COM6",  baudrate=9600, timeout=.1)


def write_read():
    #arduino.write(bytes(x,  'utf-8'))
    time.sleep(0.005)
    data = arduino.readline()
    return  data

eventos=[]
start = time.time()
elapsed=0
print("midiendo")
while elapsed<5:
    value  = write_read()
    value = str(value).replace("'","").replace("b","")
    value = value.replace("\\r","")
    value = value.replace("\\n","")
    eventos.append(value)
    end = time.time()
    elapsed = end-start

pass
