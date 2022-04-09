p = [list(map(int,input().split())) for _ in range(3)]
a,b = [p[0][0] - p[1][0], p[0][1] - p[1][1]],[p[1][0] - p[2][0], p[1][1] - p[2][1]]
doc = a[0] * b[1] - a[1] * b[0]
print(1 if doc > 0 else ( 0 if doc == 0 else -1))