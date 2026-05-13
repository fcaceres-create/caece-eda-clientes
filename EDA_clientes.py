# =============================================================================
# Actividad N°3 - Mi primer EDA
# Análisis exploratorio del dataset clientes.csv
# =============================================================================

# Importación de librerías necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carga del dataset
df = pd.read_csv("clientes.csv")


# -----------------------------------------------------------------------------
# PASO 1: Un primer vistazo
# Resumen estadístico básico de todas las variables numéricas.
# -----------------------------------------------------------------------------
print("=" * 60)
print("PASO 1 - Resumen estadístico (df.describe)")
print("=" * 60)
print(df.describe())

print("\n" + "=" * 60)
print("Información general del dataset (df.info)")
print("=" * 60)
df.info()


# -----------------------------------------------------------------------------
# PASO 2: Manipulación de datos
# Filtrar clientes con ingresos > 50.000, agrupar por estado_civil
# y calcular la media de los ingresos por grupo.
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("PASO 2 - Clientes de alto valor (ingresos > 50.000)")
print("=" * 60)

# Filtrado
clientes_alto_valor = df[df["ingresos"] > 50000]
print(f"\nCantidad de clientes con ingresos mayores a $50.000: {len(clientes_alto_valor)}")
print("\nClientes filtrados:")
print(clientes_alto_valor)

# Agrupación por estado civil y cálculo de la media de ingresos
media_ingresos_por_estado = clientes_alto_valor.groupby("estado_civil")["ingresos"].mean()
print("\nMedia de ingresos por estado civil (solo clientes de alto valor):")
print(media_ingresos_por_estado.round(2))


# -----------------------------------------------------------------------------
# PASO 3: Exploración visual
# 1) Histograma de la variable edad.
# 2) Scatter plot de ingresos (X) vs monto_compra (Y).
# -----------------------------------------------------------------------------

# Gráfico 1: Histograma de edad
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="edad", bins=6, color="#2a6e57", edgecolor="white")
plt.title("Distribución de edad de los clientes")
plt.xlabel("Edad")
plt.ylabel("Cantidad de clientes")
plt.tight_layout()
plt.savefig("histograma_edad.png", dpi=100, bbox_inches="tight")
plt.show()

# Gráfico 2: Scatter plot de ingresos vs monto_compra
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="ingresos", y="monto_compra",
                hue="genero", s=100, palette="Set1")
plt.title("Relación entre ingresos y monto de compra")
plt.xlabel("Ingresos ($)")
plt.ylabel("Monto de compra ($)")
plt.tight_layout()
plt.savefig("scatter_ingresos_compra.png", dpi=100, bbox_inches="tight")
plt.show()
