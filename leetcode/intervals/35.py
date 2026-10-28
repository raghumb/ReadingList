# Find the minimum number of intervals need to be removed to
# make the rest of the intervals non-overlapping.

"""Given a 2D array intervals[][], where intervals[i] = [starti, endi]. 
    Find the minimum number of intervals need to be removed to make the rest of the intervals non-overlapping.

Note: Two intervals are considered non-overlapping 
if the end time of one interval is less than or equal to the start time of the next interval.
    """
    

def eraseOverlapIntervals(intervals):
    # Why sort by ending time? 
    # We prefer to keep intervals that finish early because they 
    # leave more room for subsequent intervals.
    intervals.sort(key=lambda x: x[1])

    count = 0
    last_end = float('-inf')

    for start, end in intervals:
        # If the current interval starts before the previous kept interval ends, the intervals overlap.
        if start < last_end:
            count += 1
        else:
            last_end = end

    return count


# Hardcoded input
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

print(eraseOverlapIntervals(intervals))
