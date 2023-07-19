import numpy as np

# Establecer la semilla para obtener resultados reproducibles
np.random.seed(42)

# Función de evaluación (rendimiento esperado)
def evaluar_cartera(pesos, rendimientos_esperados):
    rendimiento_cartera = np.dot(pesos, rendimientos_esperados)
    return rendimiento_cartera

# Configuración inicial
num_activos = 5
poblacion_inicial = 10
iteraciones = 1000
peso_mutation = 0.05

# Datos históricos de rendimiento de activos (ficticios)
rendimientos_esperados = np.array([0.12, 0.05, 0.08, 0.07, 0.09])  # Ejemplo de rendimientos esperados

# Establecer la semilla para obtener la misma población inicial en cada ejecución
np.random.seed(42)

# Generación de la población inicial
poblacion = np.random.rand(poblacion_inicial, num_activos)
poblacion = poblacion / np.sum(poblacion, axis=1, keepdims=True)  # Asegurar que los pesos sumen 1 en cada individuo
poblacion = np.abs(poblacion)  # Convertir cualquier número negativo en su valor absoluto

# Evaluación de la población inicial
aptitudes = []
for i, individuo in enumerate(poblacion):
    aptitud = evaluar_cartera(individuo, rendimientos_esperados)
    aptitudes.append(aptitud)
    print("Individuo", i+1, ":", np.round(individuo * 100, 2), " - Aptitud:", np.round(aptitud * 100, 2))

# Bucle principal del algoritmo genético
for iteracion in range(iteraciones):
    # Selección de los padres mediante la ruleta de selección
    probabilidades_seleccion = np.array(aptitudes)
    probabilidades_seleccion /= np.sum(probabilidades_seleccion)  # Normalizar las probabilidades
    padres_indices = np.random.choice(range(poblacion_inicial), size=poblacion_inicial, replace=True, p=probabilidades_seleccion)

    # Creación de la nueva generación (cruce y mutación)
    nueva_generacion = []
    for i in range(poblacion_inicial):
        padre_1 = poblacion[padres_indices[i]]
        padre_2 = poblacion[np.random.choice(padres_indices)]
        
        # Cruce en un punto
        punto_cruce = np.random.randint(num_activos)
        hijo = np.concatenate((padre_1[:punto_cruce], padre_2[punto_cruce:]))

        # Mutación
        for j in range(num_activos):
            if np.random.rand() < peso_mutation:
                hijo[j] += np.random.uniform(-0.1, 0.1)
        
        hijo = np.abs(hijo)  # Convertir cualquier número negativo en su valor absoluto
        hijo /= np.sum(hijo)  # Asegurar que los pesos sumen 1

        nueva_generacion.append(hijo)

    # Actualización de la población y aptitudes
    poblacion = np.array(nueva_generacion)
    aptitudes = [evaluar_cartera(individuo, rendimientos_esperados) for individuo in poblacion]

# Resultado final
mejor_individuo_index = np.argmax(aptitudes)
mejor_individuo = poblacion[mejor_individuo_index]
mejor_aptitud = aptitudes[mejor_individuo_index]

# Imprimir resultados en porcentaje
print("Resultados finales:")
print("Mejor cartera de inversión encontrada:")
print(np.round(mejor_individuo * 100, 2))
print("Rendimiento esperado de la cartera:")
print(np.round(mejor_aptitud * 100, 2))
