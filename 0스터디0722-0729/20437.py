import sys; input = sys.stdin.readline
for _ in range(int(input())) :
  w,k= input().strip(),int(input())
  ww,len_list = {},[]
  for i,str in enumerate(w) :
    if str in ww : ww[str].append(i)
    else : ww[str] = [i]
  for str in ww :
    str_idx_list = ww[str]
    n = len(str_idx_list)
    if n < k : continue
    for i in range(n-k+1) :
      len_ = str_idx_list[i+k-1] - str_idx_list[i] + 1
      len_list.append(len_)
  if len_list : print(min(len_list),max(len_list))
  else : print(-1)