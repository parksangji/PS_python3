import sys; from collections import deque ; n,k = map(int,sys.stdin.readline().split())

belt = deque(list(map(int,sys.stdin.readline().split())))
robot = deque([0] * (n))

answer = 0

while 1 :
  belt.rotate(1) 
  robot.rotate(1)
  robot[-1] = 0
  if sum(robot)  :
    for i in range(n-2,-1,-1) :
      if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1 :
        robot[i+1] = 1
        robot[i] = 0
        belt[i+1] -= 1
    robot[-1] = 0
  if robot[0] == 0 and belt[0] >= 1 :
    robot[0] = 1
    belt[0] -= 1
  answer += 1
  if belt.count(0) >= k :
    break
print(answer)