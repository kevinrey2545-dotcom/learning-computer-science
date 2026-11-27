#this code sums groups of three numbers. 
import sys
datos = [int(x) for x in sys.stdin.read().split()]
def suma(a, b, c):
    return a + b + c
for i in range (datos[0]):
    print(f"{suma(datos[1], datos[2], datos[3])} ")
    for i in range (3):
        datos.pop(1)
