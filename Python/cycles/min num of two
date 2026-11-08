# A Python solution that reads pairs of numbers from standard input, compares them, and outputs the lower number for each test case. It handles CodeAbbey's input format where the first line indicates the total number of test iterations.
import sys
lineas = [int(x) for x in sys.stdin.read().split()]
def sum(a, b):
    if a > b:
        return b
    else:
        return a
final = []
for i in range(lineas[0]):
    final.append(sum(lineas[1], lineas[2]))
    lineas.pop(1)
    lineas.pop(1)
while final != []:
    print(f"{final[0]} ")
    final.pop(0)
