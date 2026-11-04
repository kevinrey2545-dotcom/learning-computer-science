# This program calculates discounts based on the total amount spent on tickets and food.
print("Digite el valor pagado en boletos:")
a = int(input())

print("Digite el valor pagado en alimentos:")
b = int(input())

c = int(((a + b) * 5) / 100)
d = int(((a + b) * 10) / 100)
e = int(((a + b) * 20) / 100)
f = int(((a + b) * 35) / 100)

def des(a, b, c, d, e, f):
    if a + b <= 40000:
        return f"Debe pagar un total de ${a + b} y no hay descuentos"
    elif a + b <= 100000:
        return f"Debe pagar un total de ${int(a + b - c)} y el descuento es de ${c}"
    elif a + b <= 200000:
        return f"Debe pagar un total de ${int(a + b - d)} y el descuento es de ${d}"
    elif a + b < 500000:
        return f"Debe pagar un total de ${int(a + b - e)} y el descuento es de ${e}"
    else:
        return f"Debe pagar un total de ${int(a + b - f)} y el descuento es de ${f}"

print(des(a, b, c, d, e, f))
