import sys
s = list(input())

ans = 0
stack = []

for i in range(len(s)) :
  if s[i] == '(' :
    stack.append('(')
  else :
    if s[i-1] == '(' :
      stack.pop()
      ans += len(stack)
    else :
      stack.pop()
      ans += 1
print(ans)
      
