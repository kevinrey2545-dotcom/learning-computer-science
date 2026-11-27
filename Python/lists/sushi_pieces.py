#Add contiguous run-length solver for Sushi for Two (CF 1138A)
n = int(input())
sushi = list(map(int, input().split()))
parejas = []
maxp = []
def par(s):
    c = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            c += 1
        else:
            parejas.append(c)
            c = 1
    parejas.append(c) 
par(sushi)
def lo(a):
    for i in range(len(parejas) - 1):
        if a[i] == a[i + 1]:
            maxp.append(a[i] + a[i + 1])
        elif a[i] != a[i + 1]:
            if a[i] > a[i + 1]:
                difer = a[i] - a[i + 1]
                maxp.append((a[i] - difer) + a[i + 1])
            else:
                difer = a[i + 1] - a[i]
                maxp.append((a[i + 1] - difer) + a[i])
lo(parejas)
print(max(maxp))
