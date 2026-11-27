#Add script to check if "hello" appears as a subsequence
obj = "hello"
pos = 0
for i in input().strip():
    if i == obj[pos]:
      pos +=1
      if pos == len(obj):
        print("SI")
        break
if pos != len(obj):
  print("NO")
