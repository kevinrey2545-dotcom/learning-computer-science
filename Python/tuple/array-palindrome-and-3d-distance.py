#A collection of fundamental algorithmic solutions in Python covering arrays, 3D geometry, loops, and functions.
def distancia(p, q):
    x1, y1, z1 = p
    x2, y2, z2 = q
    return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** (1/2)
print(f"{distancia(tuple(map(float, input().split())), tuple(map(float, input().split()))):.6f}")
