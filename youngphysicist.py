# codeforces problem: Young Physicist 69A
n= int(input())
# Initialize the sum of forces in x, y, and z directions
x_sum = 0
y_sum = 0
z_sum = 0
for _ in range(n):
    x,y,z= map(int, input().split())
    x_sum +=x
    y_sum +=y
    z_sum +=z
# Check if the net force is zero in all three directions
if x_sum == 0 and y_sum == 0 and z_sum == 0:
    print("YES")
else:
    print("NO")




