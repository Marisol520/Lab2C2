import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset de libros
df2 = pd.read_csv('libros_completos.csv')

# Asegurarse de que las columnas están en minúsculas para evitar errores
df2.columns = df2.columns.str.lower()

# Limpiar la columna de precio y convertirla a tipo numérico
df2['precio'] = df2['precio'].replace({'\$': '', ',': ''}, regex=True).astype(float)

# Verificar y limpiar los nombres de las categorías
df2['categoria'] = df2['categoria'].str.strip().str.lower()  # Eliminar espacios y convertir a minúsculas

# Mostrar los conteos de cada categoría para identificar problemas
conteo_categorias = df2['categoria'].value_counts()
print("\nConteo de libros por categoría:")
print(conteo_categorias)

# Calcular el precio promedio por categoría
precio_categoria = df2.groupby('categoria')['precio'].mean().reset_index()

# Gráfico de Barras: Precio promedio de libros por categoría
plt.figure(figsize=(12, 6))
sns.barplot(data=precio_categoria, x='categoria', y='precio', hue='categoria', palette='viridis', legend=False)
plt.title('Precio Promedio de Libros por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Precio Promedio')
plt.xticks(rotation=45)
plt.tight_layout()  # Ajustar el diseño para evitar que se corten las etiquetas
plt.show()

# Análisis
print("\nEste gráfico de barras muestra el precio promedio de los libros agrupados por categoría.")
print("Las siguientes columnas están disponibles en el dataset:")

# Mostrar todas las columnas en el mismo orden
columnas = ['titulo', 'autor', 'precio', 'categoria']
for col in columnas:
    print(f"- {col.capitalize()} (primeros 5):", df2[col].unique()[:5])  # Muestra los primeros 5 valores únicos de cada columna

print("Se puede observar qué categorías tienen precios más altos o más bajos en promedio.")

# Enlace al dataset de Kaggle (reemplazar por enlace real)
print("Enlace dataset 2: https://www.kaggle.com/datasets/hykevin2/libros-completos ")