# Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Calculate happiness
happiness = 0
for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

# Print result
print(happiness)