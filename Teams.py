# codeforces 231A Teams problem solution
# Take the number of teams as input
n = int(input())  # number of teams
count = 0  # Initialize the count of teams that can solve the problem

for _ in range(n):
    # Read the number of members who can solve the problem for each team
    a, b, c = map(int, input().split())
    # Check if at least two members can solve the problem
    if a + b + c >= 2:
        count += 1  # Increment the count if condition is met

print(count)