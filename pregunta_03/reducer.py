import sys

# Leer los datos de la entrada estándar
lines = sys.stdin.readlines()

# Ordenar las líneas por la clave (segunda columna)
sorted_lines = sorted(lines, key=lambda x: int(x.strip().split('\t')[0]))

# Imprimir las líneas ordenadas
for line in sorted_lines:
    sys.stdout.write(line.split('\t')[1])