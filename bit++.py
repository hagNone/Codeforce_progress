#codeforce 282A bit++ solution
# Take the number of operations as input
n= int(input())
count = 0

for _ in range(n):
    operations= input().strip()
    # Check if the operation is increment or decrement
    if operations== "X++" or operations== "++X":
        count +=1
    elif operations== "X--" or operations== "--X":
        count -=1

print(count) 
