import sys

# Iterar sobre cada línea de entrada
for row in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en campos
    campos = row.strip().split()

    # Verificar si la línea tiene el número correcto de campos
    if len(campos) == 3:
        clave = campos[0]
        fecha = campos[1]
        valor = float(campos[2])

        # Emitir el par clave-valor al stdout
        sys.stdout.write("{}\t{}\t{}\n".format(clave, fecha, valor))
