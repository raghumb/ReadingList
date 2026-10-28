# Insert a new interval into a sorted list of non-overlapping intervals and merge overlaps
# sorted by start time

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]

result = []
i = 0
n = len(intervals)

# Step 1: Add intervals that come before the new interval
while i < n and new_interval[0] > intervals[i][1]:
    result.append(intervals[i])
    i += 1

# Step 2: Merge overlapping intervals
while i < n and intervals[i][0] <= new_interval[1]:
    new_interval[0] = min(new_interval[0], intervals[i][0])
    new_interval[1] = max(new_interval[1], intervals[i][1])
    i += 1

result.append(new_interval)

# Step 3: Add the remaining intervals
while i < n:
    result.append(intervals[i])
    i += 1

print(result)
