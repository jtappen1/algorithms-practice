"""
Sliding Window Problem Collection
Each function implements a Sliding Window problem and has its own test cases at the bottom.
"""

from typing import List

# ----------------------
# Problem 15: 3Sum
# ----------------------
def threeSum(nums: List[int]) -> List[List[int]]:
        # Sort done in O(nlogn)
        nums = sorted(nums)
        ans = []
        # Scan through with first index takes O(n) time worst case.
        for i in range(len(nums)):
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            left , right  = i + 1, len(nums) -1
            # Scanning over the remaining elements will equal approximately O(n)
            # Each element in the n-1 elements is scanned over once.  However this is increasingly shrunk down
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                    while left < right and nums[right] == nums[right +1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -=1
        
        return ans
# Best = Worst = Average Case TC:  O(n^2)
# Space Complexity: O(n^2), using a list to hold n^2 triplet pairs in the worst case.

# Notes: 
# - If its identified that the worst case is something like O(n^3), think about if you can reduce time complexity by 
# sorting the input.



