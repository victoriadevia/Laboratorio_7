import pandas as pd
import matplotlib.pyplot as plt

ruta_archivo = 'eventos_50mil_1mil_5seg.csv'

df = pd.read_csv(ruta_archivo)

print(df.head())
print(df.columns)
df_filled = df.fillna(0)
print("\nDataFrame con NaN reemplazados por 0:")
print(df_filled)

#df_filled.plot()
#plt.figure(figsize=(10, 5))
ax = df_filled.plot()

# Configurar los nombres de los ejes y el título de la gráfica
ax.set_xlabel('Milisegundos')
ax.set_ylabel('Bits')
ax.set_title('Comportamiento del Sensor respecto al Led')

# Configurar la leyenda
ax.legend(['Sensor' , 'Led'])

# Mostrar la gráfica
plt.show()



