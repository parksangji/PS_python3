import sys,math; input = sys.stdin.readline
n = int(input());arr = list(map(int,input().split()));b,c = map(int,input().split())
print(sum([math.ceil(max(0,i-b)/c) for i in arr]) + n)