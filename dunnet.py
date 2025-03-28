import pandas as pd
from scipy import stats

# Cargar los datos
df = pd.read_excel('C:\\Agus\\2025 1er cuatri\\Io2\\tp 1\\datos_dunnet.xlsx')

def realizar_test_dunnett(datos, control='E1_2JUG'):
    # Crear listas para almacenar resultados
    grupos = []
    valores = []
    
    # Preparar datos para el análisis
    for columna in datos.columns:
        if columna != control:
            grupos.extend([control] * len(datos[control]))
            grupos.extend([columna] * len(datos[columna]))
            valores.extend(datos[control].dropna())
            valores.extend(datos[columna].dropna())
    
    # Realizar ANOVA primero
    grupos_unicos = datos.columns
    f_stat, p_valor_anova = stats.f_oneway(*[datos[col].dropna() for col in grupos_unicos])
    
    # Realizar comparaciones múltiples con Dunnett
    resultados = []
    control_data = datos[control].dropna()
    
    for columna in datos.columns:
        if columna != control:
            grupo_data = datos[columna].dropna()
            t_stat, p_valor = stats.ttest_ind(control_data, grupo_data)
            resultados.append({
                'Grupo': columna,
                'Estadístico-t': t_stat,
                'p-valor': p_valor
            })
    
    # Convertir resultados a DataFrame
    resultados_df = pd.DataFrame(resultados)
    
    # Aplicar corrección de Bonferroni
    resultados_df['p-valor ajustado'] = resultados_df['p-valor'] * (len(datos.columns) - 1)
    resultados_df['Significativo'] = resultados_df['p-valor ajustado'] < 0.05
    
    return {
        'ANOVA': {
            'F-estadístico': f_stat,
            'p-valor': p_valor_anova
        },
        'Comparaciones': resultados_df
    }

# Ejecutar el análisis
resultados = realizar_test_dunnett(df)

# Mostrar resultados
print("\nResultados del ANOVA:")
print(f"F-estadístico: {resultados['ANOVA']['F-estadístico']:.4f}")
print("Comparación de medias contra el control (95% confianza):")
for idx, row in resultados['Comparaciones'].iterrows():
    control_mean = df['E1_2JUG'].mean()
    grupo_mean = df[row['Grupo']].mean()
    diferencia = grupo_mean - control_mean
    print(f"{row['Grupo']}: Media = {grupo_mean:.2f} vs Control ({control_mean:.2f})")
    print(f"Diferencia: {diferencia:.2f} {'(Mayor)' if diferencia > 0 else '(Menor)'}")
print(f"p-valor: {resultados['ANOVA']['p-valor']:.4f}")

print("\nComparaciones contra el control (E1_2jug):")
print(resultados['Comparaciones'].to_string(index=False))

# Crear visualización de los resultados
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.title('Comparación de grupos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Guardar resultados en un archivo
resultados['Comparaciones'].to_csv('resultados_dunnett.csv', index=False)

