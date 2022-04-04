
string = str(input())

flag = False

plus = 0
minus = 0
tmp = ""

for ch in string :
  # print(plus,minus,tmp)
  if ch == "-" or ch == "+":
      if flag :
        minus += int(tmp)
      else :
        plus += int(tmp)
      tmp = ""
      if ch == '-' :
        flag = True
  else :
    tmp += ch
if flag and tmp != "" :
  minus += int(tmp)
elif not flag and tmp != "":
  plus += int(tmp)

print(plus - minus)
    