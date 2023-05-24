import sys

# Inicializar el diccionario para almacenar los conteos de credit_history
credit_counts = {}

# Leer los datos de la entrada estándar
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en clave y valor
    credit_history, count = line.strip().split('\t')

    # Convertir el conteo a entero
    count = int(count)

    # Incrementar el contador para el tipo de credit_history actual
    if credit_history in credit_counts:
        credit_counts[credit_history] += count
    else:
        credit_counts[credit_history] = count

# Imprimir los resultados
for credit_history, count in credit_counts.items():
    print(f'{credit_history}\t{count}')
