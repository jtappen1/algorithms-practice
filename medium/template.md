"""
Dynamic Programming Problem Collection
Each function implements a DP problem and has its own test cases at the bottom.
"""

from typing import List

# ----------------------
# Problem 1: Climbing Stairs
# ----------------------
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# ----------------------
# Problem 2: Min Cost Climbing Stairs
# ----------------------
def min_cost_climbing_stairs(cost: List[int]) -> int:
    n = len(cost)
    dp = cost[:]
    for i in range(2, n):
        dp[i] += min(dp[i-1], dp[i-2])
    return min(dp[-1], dp[-2])

# ----------------------
# Add more DP problems here...
# ----------------------


# ----------------------
# Test cases
# ----------------------
if __name__ == "__main__":
    # Climbing stairs
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3

    # Min cost climbing stairs
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

    print("All DP tests passed!")