import sys

current_credit_history = None
credit_history_count = 0

# Itera sobre las líneas de entrada
for line in sys.stdin:
    # Elimina espacios en blanco y divide por tabulaciones
    credit_history, count = line.strip().split('\t')
    
    # Si es la misma clave que antes, incrementa el contador
    if current_credit_history == credit_history:
        credit_history_count += int(count)
    else:
        # Si es una clave diferente, imprime el resultado del atributo anterior (si no es None)
        if current_credit_history is not None:
            print(current_credit_history + '\t' + str(credit_history_count))
        
        # Reinicia las variables para la nueva clave
        current_credit_history = credit_history
        credit_history_count = int(count)

# Imprime el resultado para la última clave
if current_credit_history is not None:
    print(current_credit_history + '\t' + str(credit_history_count))
