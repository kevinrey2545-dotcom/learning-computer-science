#Add alternating phrase generator for Codeforces 705A (Hulk)
n = int(input())
emo = []
if n == 1 :
    emo.append("I hate it")
elif n%2 == 0:
    for i in range (n//2):
        emo.append("I hate that")
        emo.append("I love that")
    emo.pop(n-1)
    emo.append("I love it")
else:
    for i in range (n//2):
        emo.append("I hate that")
        emo.append("I love that")
    emo.append("I hate it")
print(" ".join(emo))
