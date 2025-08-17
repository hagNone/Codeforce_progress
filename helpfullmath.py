# Codeforces 339A - Helpful Maths

s = input()   #take input as string,
nums = sorted(map(int, s.split("+")))   # split by '+', convert to int, sort
result = "+".join(map(str, nums))       # join back with '+'
print(result)