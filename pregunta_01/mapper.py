import sys
import csv

# Leer el archivo CSV desde la entrada estándar
reader = csv.reader(sys.stdin)

# Obtener los encabezados
headers = next(reader)

# Obtener el índice del atributo 'credit_history'
credit_history_index = headers.index('credit_history')

# Emitir el nombre de la columna como un registro
print('credit_history\t1')

# Iterar sobre cada línea de entrada
for row in reader:
    # Verificar si la fila tiene el número correcto de campos
    if len(row) == len(headers):
        # Obtener el valor del atributo 'credit_history'
        credit_history = row[credit_history_index]
        
        # Emitir el par clave-valor al stdout
        print(f'{credit_history}\t1')
