#Parses DD/MM/YYYY date strings into comparable (YYYY, MM, DD) tuples to find and print the oldest and most recent dates in a single pass.
def convertir(texto):
    d, m, a = map(int, texto.split("/"))
    return (a, m, d)

def extremos(fechas):
    antigua = reciente = fechas[0]
    for f in fechas:
        if f < antigua: antigua = f
        if f > reciente: reciente = f
    return (antigua, reciente)

fechas = tuple(convertir(input()) for _ in range(int(input())))
antigua, reciente = extremos(fechas)

for a, m, d in (antigua, reciente):
    print(f"{d:02d}/{m:02d}/{a:04d}")
