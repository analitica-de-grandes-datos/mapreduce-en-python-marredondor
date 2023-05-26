import sys

# Leer el contenido de la entrada estándar
data = sys.stdin.read()

# Eliminar saltos de línea adicionales
data = data.strip()

# Dividir el contenido en líneas
lines = data.split('\n')

# Iterar sobre cada línea de entrada
for line in lines:
    # Eliminar espacios en blanco y dividir la línea en campos
    fields = line.strip().split(',')

    # Verificar si la línea tiene el número correcto de campos
    if len(fields) == 2:
        # Obtener el valor de la segunda columna
        column2_value = int(fields[1])

        # Emitir el par clave-valor al stdout
        sys.stdout.write("{}\t{}\n".format(column2_value, line))