""" 
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.
Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num_dict.get(str(num)):
                return True
            else:
                num_dict.update({str(num) : 1})
        return False


if __name__ == '__main__':
    nums1 = [1,2,3,1]
    print(Solution().containsDuplicate(nums1))
    nums2 = [1,2,3,4]
    print(Solution().containsDuplicate(nums2))
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    print(Solution().containsDuplicate(nums3))
