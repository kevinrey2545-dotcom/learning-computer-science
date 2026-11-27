# multiplication tables generator (1 to 11)
for i in range(1,12):
    for j in range(1,11):
        print(i, "x", j, "=", i * j)
    if i<11:
      print()
