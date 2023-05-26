import sys

# Inicializar el diccionario para almacenar los valores máximos de amount por purpose
max_amounts = {}

# Leer los datos de la entrada estándar
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en clave y valor
    purpose, amount = line.strip().split('\t')
    amount = int(amount)

    # Actualizar el valor máximo de amount para cada purpose
    if purpose in max_amounts:
        max_amounts[purpose] = max(max_amounts[purpose], amount)
    else:
        max_amounts[purpose] = amount

# Imprimir los resultados
for purpose in sorted(max_amounts.keys()):
    max_amount = max_amounts[purpose]
    sys.stdout.write("{}\t{}\n".format(purpose, max_amount))