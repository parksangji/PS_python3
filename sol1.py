
"""
첫째 줄에 몬스터의 수 $N$과 시루의 초기 체력 $K$가 공백으로 구분되어 주어진다.

둘째 줄에 각 마을에 있는 몬스터의 공격력 $A_1, A_2, \cdots, A_N$이 공백으로 구분되어 주어진다.

셋째 줄에 각 마을에 있는 주민의 수 $P_1, P_2, \cdots, P_N$이 공백으로 구분되어 주어진다.
"""

import sys; input = sys.stdin.readline


n,k = map(int,input().split())
A = list(map(int,input().split()))
P = list(map(int,input().split()))
board = [(a,b) for a,b in zip(A,P)]
print(board)