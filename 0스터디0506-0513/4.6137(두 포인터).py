import sys; n = int(sys.stdin.readline())

s = ''.join([sys.stdin.readline().strip() for _ in range(n)]) ; t = ''
i,j,cnt = 0,n-1,0
while i <= j :
  if s[i] < s[j] : t += s[i] ; i+= 1
  elif s[i] > s[j] : t += s[j] ; j -= 1
  else :
    ii,jj = i,j
    while ii <= jj :
      if s[ii] < s[jj] :
        t += s[i]; i += 1
        break
      elif s[ii] > s[jj] :
        t += s[j]; j -= 1
        break
      else :
        ii += 1 ; jj -= 1
    else :
      t += s[i] ; i += 1
  cnt += 1
  if cnt % 80 == 0 :
    t += '\n'
print(t)