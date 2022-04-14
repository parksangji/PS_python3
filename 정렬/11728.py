import sys
input()
print(' '.join(sorted(sys.stdin.read().split(), key=int)))