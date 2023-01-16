"""
You are given an integer array nums. The absolute sum of a
subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:
    If x is a negative integer, then abs(x) = -x.
    If x is a non-negative integer, then abs(x) = x.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        local_max = 0
        global_max = float('-inf')
        for i in range(len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(global_max, local_max)

        local_min = 0
        global_min = float('inf')
        for i in range(len(nums)):
            local_min = min(nums[i], nums[i] + local_min)
            global_min = min(global_min, local_min)
        return max(abs(global_max), abs(global_min))


if __name__ == '__main__':
    sol = Solution()
    nums = [1, -3, 2, 3, -4]
    print(sol.maxAbsoluteSum(nums))
    nums2 = [2, -5, 1, -4, 3, -2]
    print(sol.maxAbsoluteSum(nums2))
