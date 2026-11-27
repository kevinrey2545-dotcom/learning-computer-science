#this code add judge score trimmer and integer average calculator
def quitar_extremos(puntajes):
    puntajes.remove(max(puntajes))
    puntajes.remove(min(puntajes))
def promedio_entero(puntajes):
    return sum(puntajes) // len(puntajes)
jueces = int(input())
datos = [int(x) for x in input().split()]
quitar_extremos(datos)
datos.sort()
print(promedio_entero(datos))
print(*datos)
