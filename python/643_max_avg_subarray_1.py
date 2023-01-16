"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. Any answer with a calculation error less than 10-5 will
be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        local_max = global_max = sum(nums[0: k])
        for i in range(len(nums) - k):
            local_max += nums[i + k] - nums[i]
            global_max = max(global_max, local_max)
        return global_max / k


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    print(sol.findMaxAverage(nums, 4))
    nums2 = [5]
    print(sol.findMaxAverage(nums2, 1))
