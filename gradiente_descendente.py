def funcion_objetivo(x):
  """
  Define la función objetivo X^2 + 5X + 6.

  Args:
    x: Valor de la variable independiente.

  Returns:
    Valor de la función objetivo en x.
  """
  return x**2 + 5 * x + 6

def derivada_funcion_objetivo(x):
  """
  Calcula la derivada de la función objetivo 2X + 5.

  Args:
    x: Valor de la variable independiente.

  Returns:
    Valor de la derivada de la función objetivo en x.
  """
  return 2 * x + 5

def gradiente_descendente(tasa_aprendizaje, num_epocas, punto_inicial):
  """
  Implementa el algoritmo del gradiente descendente para encontrar el mínimo de la función objetivo.

  Args:
    tasa_aprendizaje: Tasa de aprendizaje del algoritmo.
    num_epocas: Número de épocas a ejecutar el algoritmo.
    punto_inicial: Punto inicial para la búsqueda del mínimo.

  Returns:
    Valor de X y Y después de las iteraciones.
  """
  x = punto_inicial
  y = funcion_objetivo(x)

  for epoca in range(num_epocas):
    # Calcula el gradiente en el punto actual
    gradiente = derivada_funcion_objetivo(x)

    # Actualiza el valor de X usando el gradiente descendente
    x_nuevo = x - tasa_aprendizaje * gradiente

    # Evalúa la función objetivo en el nuevo valor de X
    y_nuevo = funcion_objetivo(x_nuevo)

    # Actualiza los valores de X e Y
    x = x_nuevo
    y = y_nuevo

  return x, y

# Casos de prueba
casos_prueba = [
  [0.1, 10, 1],
  [0.2, 20, 0],
  [0.1, 50, 3],
]

for caso in casos_prueba:
  tasa_aprendizaje, num_epocas, punto_inicial = caso
  x, y = gradiente_descendente(tasa_aprendizaje, num_epocas, punto_inicial)
  print(f"{x:.6f} {y:.6f}")
