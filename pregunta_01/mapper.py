import sys

# Leer el contenido de la entrada estándar
data = sys.stdin.read()

# Eliminar saltos de línea adicionales
data = data.strip()

# Dividir el contenido en líneas
lines = data.split('\n')

# Iterar sobre cada línea de entrada
for line in lines:
    # Elimina espacios en blanco y divide la línea en campos
    fields = line.strip().split(',')

    # Verifica si la línea tiene el número correcto de campos
    if len(fields) == 21:
        # Obtiene el valor del atributo 'credit_history'
        credit_history = fields[2]

        # Emite el par clave-valor al stdout
        print(f'{credit_history}\t1')
