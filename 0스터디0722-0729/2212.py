n,k,*x = map(int,open(0).read().split()) ;x.sort()
print(sum(sorted([x[i+1] - x[i] for i in range(n-1)])[:n-k]))