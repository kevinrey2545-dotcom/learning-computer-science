#Add accidental Caps Lock text fixer
palabra = input().strip()
letras = list(palabra)
todas_mayus_desde_segunda = True
for i in range(1, len(letras)):
    if letras[i].islower():
        todas_mayus_desde_segunda = False
        break
if todas_mayus_desde_segunda:
    for i in range(len(letras)):
        if letras[i].isupper():
            letras[i] = letras[i].lower()
        else:
            letras[i] = letras[i].upper()
print("".join(letras))
