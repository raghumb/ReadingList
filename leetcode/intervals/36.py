#  Merge Intervals
"""
    You are given an array intervals where intervals[i] = [startᵢ, endᵢ] represents the inclusive interval startᵢ ≤ x ≤ endᵢ.

Your task is to merge every pair of intervals that overlap and return all the non-overlapping intervals that completely cover the same ranges as the original array.

Two intervals overlap if they share at least one common point (i.e. start₂ ≤ end₁ and start₁ ≤ end₂).

Return the merged intervals in any order.
    """
    
    

def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []

    for start, end in intervals:
        # No overlap with the previous interval
        # This checks whether the current interval starts after the last merged interval ends.
        """
            merged[-1] → gets the last interval: [12, 15]
            merged[-1][1] → gets the element at index 1 of [12, 15], which is 15.
        """
        
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            # Merge overlapping intervals
            merged[-1][1] = max(merged[-1][1], end)

    return merged


# Hardcoded input
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(merge(intervals))
