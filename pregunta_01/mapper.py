import sys

for l in sys.stdin:
  lista = l.split(",")
  nombre = lista[2]
  sys.stdout.write(nombre+"\t1\n")
