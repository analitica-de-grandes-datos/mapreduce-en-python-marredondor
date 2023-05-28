import sys

# Inicializar una lista para almacenar los valores de la tercera columna
values = []

# Iterar sobre cada línea de entrada
for row in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en campos
    campos = row.strip().split()

    # Verificar si la línea tiene el número correcto de campos
    sys.stdout.write("{}\t{}\t{}".format(row.split("   ")[0],row.split("   ")[1],row.split("   ")[2]))