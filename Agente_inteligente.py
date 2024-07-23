def agente_ascii(percepcion):
    return ' '.join(str(ord(char)) for char in percepcion)

# Leer la entrada
entrada = input()

# Procesar la entrada y obtener la salida
salida = agente_ascii(entrada)

# Imprimir el resultado
print(salida)