import sys

for line in sys.stdin:
    columnas=line.split(" ")
    columna1= columnas[0]
    columna2= columnas[3]
    columna3= int(columnas[6])
    sys.stdout.write(f"{columna1}\t{columna2}\t{columna3}\n")
