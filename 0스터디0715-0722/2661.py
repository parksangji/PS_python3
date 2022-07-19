def dfs(s,cnt,depth) :
  global flag
  print(s)
  if flag : return
  for i in range(1,len(s)//2+1) :
    if s[len(s)-i : len(s)-i + i] == s[len(s) - 2*i :len(s) - 2*i + i] :
      s= ""
      return
  if cnt > depth : return
  if cnt == depth :
    flag = True
    print(s)
    return
  else :
    for i in range(depth) :
      dfs(s + "1", cnt + 1,depth)
      dfs(s + "2", cnt + 1,depth)
      dfs(s + "3", cnt + 1,depth)

flag = False
dfs("",0,int(input()))