input();shot = [0] * (1000000+1)
for h in list(map(int,input().split())) :
  if shot[h] > 0: shot[h] -= 1
  shot[h-1] += 1
print(sum(shot))