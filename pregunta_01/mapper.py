import sys

# Itera sobre las líneas de entrada
for line in sys.stdin:
    # Elimina espacios en blanco y divide por comas
    data = line.strip().split(',')
    
    # Extrae el valor del atributo "credit_history" (suponiendo que es el tercer atributo)
    credit_history = data[2]
    
    # Genera la salida en formato clave-valor: (credit_history, 1)
    print(credit_history + '\t' + '1')
