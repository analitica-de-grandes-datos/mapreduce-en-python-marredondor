import sys

# Inicializar el diccionario para almacenar los valores máximo y mínimo de la tercera columna por letra
max_values = {}
min_values = {}

# Leer los datos de la entrada estándar
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en clave y valor
    clave, valor = line.strip().split('\t')
    valor = float(valor)

    # Actualizar el valor máximo y mínimo para cada letra
    if clave in max_values:
        max_values[clave] = max(max_values[clave], valor)
        min_values[clave] = min(min_values[clave], valor)
    else:
        max_values[clave] = valor
        min_values[clave] = valor

# Imprimir los resultados
for clave in sorted(max_values.keys()):
    max_valor = max_values[clave]
    min_valor = min_values[clave]
    sys.stdout.write("{}\t{}\t{}\n".format(clave, max_valor, min_valor))