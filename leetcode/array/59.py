# Combination Sum

"""
    Given an array of distinct integers candidates
    and a target integer target, return a list of all unique combinations 
    of candidates where the chosen numbers sum to target. 
    You may return the combinations in any order.
    """
    
"""
    Optimal approach: Backtracking
Time complexity: Exponential in the worst case, commonly bounded by \(O(N^{T/M})\) for the search, where \(N\) is the number of candidates, \(T\) is the target, and \(M\) is the smallest candidate.

Space complexity: \(O(T/M)\) auxiliary recursion space, excluding results.
    """
    

def backtrack(candidates, start, remaining, path, result):

    if remaining == 0:
        result.append(path.copy())
        return

    if remaining < 0:
        return

    for i in range(start, len(candidates)):

        # Choose
        path.append(candidates[i])

        # Explore
        backtrack(candidates, i, remaining - candidates[i], path, result)

        # Backtrack (undo choice)
        path.pop()


def combination_sum(candidates, target):

    result = []

    backtrack(candidates, 0, target, [], result)

    return result


candidates = [2, 3, 6, 7]
target = 7

print(combination_sum(candidates, target))
