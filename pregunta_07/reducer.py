import sys

# Leer los datos de la entrada estándar y almacenarlos en una lista
datos = []
for line in sys.stdin:
    columnas = line.strip().split("\t")
    datos.append(columnas)

# Ordenar la lista por letra (columna 1) y valor (columna 3)
organizar = sorted(datos, key=lambda x: (x[0], int((x[2]))))

# Imprimir los resultados
for item in organizar:
    sys.stdout.write("{}\t{}\t{}\n".format(item[0], item[1], item[2]))
    
# Agregar las líneas adicionales
sys.stdout.write("")