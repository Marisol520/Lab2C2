import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

df3 = pd.read_csv('artists-data.csv')

# Asegurarse de que las columnas están en minúsculas para evitar errores
df3.columns = df3.columns.str.lower()

# Asegurarse de que no haya valores nulos en la columna 'genres'
df3['genres'].dropna(inplace=True)

# Gráfico Circular: Proporción de géneros
generos = df3['genres'].str.split(';', expand=True).stack().value_counts()

# Seleccionar los géneros más populares
top_generos = generos.nlargest(20)

# Agrupar otros géneros en la categoría 'Otros'
otros = generos[20:].sum() if len(generos) > 20 else 0
if otros > 0:
    top_generos = pd.concat([top_generos, pd.Series({'Otros': otros})])

# Ordenar las categorías por frecuencia
top_generos = top_generos.sort_values(ascending=False)

# Generar colores diferentes para cada categoría
colores = plt.cm.tab20(np.arange(len(top_generos))) 

# Configuración del gráfico
plt.figure(figsize=(10, 10))

# Añadir el título del gráfico
plt.title('Proporción de Géneros Musicales', pad=30, fontsize=16, fontweight='bold')

# Crear el gráfico circular
wedges, texts, autotexts = plt.pie(
    top_generos,
    labels=top_generos.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    textprops=dict(color="black")  
)

for i, (wedge, autotext) in enumerate(zip(wedges, autotexts)):
    # mostrar el porcentaje horizontalmente en la categoria "otros"
    if texts[i].get_text() == 'Otros':
        autotext.set_rotation(0) 
        autotext.set_ha('center')
    else:
        autotext.set_rotation((wedge.theta1 + wedge.theta2) / 2) 
        autotext.set_ha('center') 

# Personalizar bordes
for wedge in wedges:
    wedge.set_linewidth(1.5) 
    wedge.set_edgecolor('white') 

# Ajustar el espaciado de los textos y el gráfico
plt.subplots_adjust(top=0.7, bottom=0.2)

# Añadir el análisis como párrafo en el gráfico
analisis_texto = (
    "El gráfico circular representa la proporción de géneros musicales en el dataset.\n"
    "Se muestran los 20 géneros más populares, y el resto se agrupan como 'Otros'."
)
plt.text(0, 1.1, analisis_texto, ha='center', va='center', fontsize=10,
         bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray', boxstyle='round,pad=1'))


# Ajustar el espacio para mover el gráfico más abajo
plt.axis('equal')

# Mostrar el gráfico
plt.show()

# Enlace del dataset 
print("https://www.kaggle.com/datasets/neisse/scrapped-lyrics-from-6-genres")
