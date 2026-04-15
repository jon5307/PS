# Read input
k, n = map(int, input().split())

# Calculate minimum and maximum times
min_time = n + 1
max_time = k * n + 1

# Print result
print(min_time, max_time)