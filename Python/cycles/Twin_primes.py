#This code outputs all twin prime pairs found in a specified interval
def es_primo(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True  

n = int(input())
k = int(input())
primos = []

for i in range(k - (n - 1)):
    if es_primo(n):  
        primos.append(n)
    n += 1

while len(primos) >= 2:
    while len(primos) >= 2 and primos[0] + 2 == primos[1]:
        print(f"{primos[0]} {primos[1]}")
        primos.pop(0)
        if len(primos) == 1:
            break
    primos.pop(0)
