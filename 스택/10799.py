string = str(input())
stack = []
total = 0

for i in range(len(string)) :
  if string[i] == "(" :
    stack.append("(")
  else :
    stack.pop()
    if string[i-1] == "(" :
      total += len(stack)
    else :
      total += 1
      
print(total)