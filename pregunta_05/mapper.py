import sys

for row in sys.stdin:
    elementos = row.strip().split(",")
    campos = elementos[0]
    column = campos.split("   ")    
    linea = column[1]
    caompos_fecha = linea.split("-")  
    mes = caompos_fecha[1]
    sys.stdout.write((mes+"\t1\n"))
