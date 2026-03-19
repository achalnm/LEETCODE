class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

'''
nums = [2,5,6,0,0,1,2]
target = 2

for num in nums:
    if num == target:
        print("Found")
        break
'''

    


'''
nums = [2,5,6,0,0,1,2]
target = 2

nums.sort()

left = 0
right = len(nums) - 1

while left < right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
        print("Found")
        break
    
    elif nums[mid] > target:
        right = mid - 1
    
    else:
        left = mid + 1
'''
