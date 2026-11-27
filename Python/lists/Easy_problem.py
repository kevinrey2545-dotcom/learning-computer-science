# this code shows if a problem is dificult or not
np = int(input())
opinion = [int(x) for x in input().split()]
for i in range (np):
    if opinion[i] == 1:
        print("DIFICIL")
        break
else:
    print("FACIL")
