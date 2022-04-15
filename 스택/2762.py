x = input()
a='(';b=')';c='[';d=']'
if x.count(a)!=x.count(b) or x.count(c)!=x.count(d):print(0)
else:
    x=x.replace('()', '+2').replace('[]', '+3').replace(a, '+(').replace(b, ')*2').replace(c, '+(').replace(d, ')*3')
    try:
      print(eval(x))
    except :
      print(0)