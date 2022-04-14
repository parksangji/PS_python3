import sys
input()
print(' '.join(sorted(list(set(sys.stdin.readline().split())),key=int)))