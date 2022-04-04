# n = str(input()) ; arr = [0] * 10

# for ch in n :
#   num = int(ch)
#   arr[num] += 1

# number = -1
# for i in range(10) :
#   if i != 6 and i != 9 :
#     number = max(number,arr[i])

# if (arr[6] + arr[9]) % 2 == 0 :
#   print(max(number,(arr[6] + arr[9])//2))
# else :
#   print(max(number,(arr[6] + arr[9])//2 + 1))


c = input().count
print(max(int(max(map(c,'1234578'))),(c('6') + c('9')+1)//2))