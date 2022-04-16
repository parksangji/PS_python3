import sys
string = sys.stdin.readline().strip()
if string.count('(') != string.count(')') or string.count('[') != string.count(']') :
  print(0)
else :
  try :
    print(eval(string.replace('()','+2').replace('[]','+3').replace('(','+(').replace(')',')*2').replace('[','+(').replace(']',')*3')))
  except :
    print(0)