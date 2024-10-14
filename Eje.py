import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset Marvel Vs DC
df1 = pd.read_csv('Marvel Vs DC NEW.csv')

print(df1.columns)
print(df1.head())

# Asegurarnos de que la columna Year es de tipo numérico
df1['Year'] = pd.to_numeric(df1['Year'], errors='coerce')

# Agrupar los datos por año y género para contar el número de películas
genre_year_count = df1.groupby(['Year', 'Genre']).size().reset_index(name='count')

# Gráfico de Líneas: Número de películas por año y género
plt.figure(figsize=(12, 6))
sns.lineplot(data=genre_year_count, x='Year', y='count', hue='Genre', marker='o')
plt.title('Número de películas por año y género (Marvel vs DC)')
plt.xlabel('Año de Lanzamiento')
plt.ylabel('Número de Películas')
plt.xticks(rotation=45)
plt.legend(title='Género')
plt.show()

# Análisis
print("Este gráfico de líneas muestra el número de películas lanzadas por año, desglosadas por género. Se puede observar cómo ha evolucionado la cantidad de películas de cada género a lo largo de los años.")

# Enlace al dataset de Kaggle (reemplazar por enlace real)
print(" Enlace a dataset 1: https://www.kaggle.com/datasets/willianoliveiragibin/marvel-vs-dc")
