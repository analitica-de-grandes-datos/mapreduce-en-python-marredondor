import sys

# Inicializar el diccionario para almacenar la suma y el contador de valores por letra
sum_values = {}
count_values = {}

# Leer los datos de la entrada estándar
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en clave y valor
    clave, valor = line.strip().split('\t')
    valor = float(valor)

    # Actualizar la suma y el contador para cada letra
    if clave in sum_values:
        sum_values[clave] += valor
        count_values[clave] += 1
    else:
        sum_values[clave] = valor
        count_values[clave] = 1

# Imprimir los resultados
for clave in sorted(sum_values.keys()):
    suma = sum_values[clave]
    count = count_values[clave]
    promedio = suma / count
    sys.stdout.write("{}\t{}\t{}\n".format(clave, suma, promedio))