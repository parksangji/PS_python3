string = str(input())
print(*sorted(string[i:] for i in range(len(string))))