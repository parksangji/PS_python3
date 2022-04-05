# import heapq
# n = int(input())

# stick = [64]

# answer = 1

# while stick :

#   s = sum(stick)

#   if s == n :
#     print(answer)
#     break
#   elif n < s :
#     min = heapq.heappop(stick)
#     a = min//2
#     s -= a
    
#     if n <= s :
#       heapq.heappush(stick,a)
#     else :
#       heapq.heappush(stick,a)
#       heapq.heappush(stick,a)
#       answer += 1

print(bin(int(input())).count('1'))