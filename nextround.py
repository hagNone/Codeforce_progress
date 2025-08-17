# codeforces 158A Next Round problem solution
# Take the number of participants and the position of the last participant to advance
n,k = map(int, input().split())
arr = list(map(int, input().split()))

# Count how many participants have scores greater than or equal to the k-th participant's score
count =0
for i in arr:
    if i >= arr[k-1] and i >0:
        count +=1

print(count) # Output the count of participants who advance to the next round

    
