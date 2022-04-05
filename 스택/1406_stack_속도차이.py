# from sys import stdin

# a = stdin.readline().strip()
# cursor = len(a)

# for _ in range(int(stdin.readline())) :
#   line = arr(stdin.readline().split())
#   if line[0] == 'L' :
#     if cursor == 0 :
#       continue
#     cursor -= 1
#   elif line[0] == 'D' :
#     if cursor == len(a) :
#       continue
#     cursor += 1
#   elif line[0] == 'B' :
#     if cursor == 0 :
#       continue
#     a = a[0:cursor-1] + a[cursor :]
#     cursor -= 1
#   elif line[0] == 'P' :
#     a = a[0:cursor] + line[1] + a[cursor:]
#     cursor += 1

# print(a)


import sys
a = list(sys.stdin.readline().strip())
b = []

n = int(sys.stdin.readline())

for _ in range(n) :
  arr = list(sys.stdin.readline().split())

  if arr[0] == 'L' :
    if a :
      b.append(a.pop())
  elif arr[0] == 'D' :
    if b :
      a.append(b.pop())
  elif arr[0] == 'B' :
    if a :
      a.pop()
  else :
    a.append(arr[1])

a.extend(reversed(b))
print(''.join(a))

