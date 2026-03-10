
'''
nums = [5,7,7,8,8,10]
target = 5
count = 1
l = []

c = -1
b = -1

for i in range(len(nums)):
    if nums[i] == target:
        if count == 1:
            c = i
            count = count + 1
        b = i


if (c != -1):
    l = [c,b]
else:
    l = [-1,-1]

print (l)
'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst():
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1  # search left side for first occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def findLast():
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1  # search right side for last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        return [findFirst(), findLast()]
