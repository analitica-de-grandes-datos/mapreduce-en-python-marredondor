import sys

# Iterar sobre cada línea de entrada recibida a través de sys.stdin
for line in sys.stdin:
    # Inicializar una lista vacía para almacenar las sublistas
    list_of_lists = []

    # Eliminar los caracteres de nueva línea y retorno de carro de la línea
    line = line.replace('\n', '')
    line = line.replace('\r', '')

    # Dividir la línea en el índice y las letras utilizando '\t' como separador
    index, letras = line.split('\t')

    # Dividir las letras en una lista utilizando ',' como separador
    letras = letras.split(',')

    # Crear sublistas con el índice y cada letra y agregarlas a la lista de listas
    for letra in letras:
        list_of_lists.append([index, letra])

    # Emitir los pares clave-valor al stdout en el formato requerido
    for pareja in list_of_lists:
        sys.stdout.write("{}\t{}\n".format(str(pareja[1]), str(pareja[0])))